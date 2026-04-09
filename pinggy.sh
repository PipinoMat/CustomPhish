#!/bin/bash
source venv39/bin/activate 2>/dev/null || echo "⚠️ Attiva venv39"
rm -f credentials.txt
python server_pinggy.py &
sleep 2
echo "🔗 PINGGY TUNNEL:"
echo "ssh -p 443 -R0:localhost:5000 a.pinggy.io"
ssh -p 443 -R0:localhost:5000 a.pinggy.io