from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            }
            h1 {
                font-size: 32px;
            }
            p {
                font-size: 18px;
                margin-top: 10px;
            }
            .status {
                margin-top: 20px;
                padding: 10px;
                background: #28a745;
                border-radius: 10px;
                display: inline-block;
            }
        </style>
    </head>
    <body>

        <div class="card">
            <h1>🚀 CI/CD Pipeline Dashboard</h1>
            <p>Project: Kubernetes Deployment</p>
            <p>Toolchain: Jenkins + Docker + Kubernetes</p>

            <div class="status">
                ✅ Pipeline Working Successfully
            </div>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)