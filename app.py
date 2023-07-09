from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def test_speed():
    try:
        st = speedtest.Speedtest()
        server = st.get_best_server()
        print(server)
        print("Realizando teste de velocidade...")
        download_speed = st.download() / 10**6
        upload_speed = st.upload() / 10**6
        ping = st.results.ping

        data = {
            'download_speed': download_speed,
            'upload_speed': upload_speed,
            'ping': ping
        }

        return jsonify(data)

    except speedtest.SpeedtestException:
        return jsonify({'error': 'Ocorreu um erro ao realizar o teste de velocidade.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
