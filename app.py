from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbits/s
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbits/s
    ping = st.results.ping

    return {
        'download_speed': download_speed,
        'upload_speed': upload_speed,
        'ping': ping
    }

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/speedtest')
def speedtest_route():
    result = run_speed_test()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
