import subprocess
subprocess.run(["playwright", "install"], check=True)

from flask import Flask, request, jsonify
import asyncio
from search_flights import fetch_flights

app = Flask(__name__)

@app.route("/ucus-bilgisi", methods=["GET"])
def ucus_bilgisi():
    from_code = request.args.get("from")
    to_code = request.args.get("to")
    date = request.args.get("date")

    if not from_code or not to_code or not date:
        return jsonify({"error": "Eksik parametre"}), 400

    results = asyncio.run(fetch_flights(from_code, to_code, date))
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)