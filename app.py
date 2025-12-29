from flask import Flask, render_template_string
import base64

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Kaik boca de 09</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #e9ecef;
            color: #333;
        }

        header {
            background: #0b3d2e;
            color: #fff;
            padding: 40px 20px;
            text-align: center;
        }

        header img {
            height: 180px;
            margin-bottom: 15px;
        }

        nav {
            margin-top: 15px;
        }

        nav a {
            color: #fff;
            margin: 0 12px;
            text-decoration: none;
            font-weight: bold;
        }

        nav a:hover {
            text-decoration: underline;
        }

        .banner {
            background: #f4f6f8;
            padding: 60px 20px;
            text-align: center;
        }

        .banner h1 {
            font-size: 42px;
            margin-bottom: 10px;
            color: #0b3d2e;
        }

        .banner p {
            font-size: 18px;
        }

        .section {
            padding: 50px 20px;
            max-width: 1000px;
            margin: auto;
        }

        .section h2 {
            color: #0b3d2e;
            margin-bottom: 20px;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .card {
            background: #fff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }

        footer {
            background: #0b3d2e;
            color: #fff;
            text-align: center;
            padding: 15px;
            margin-top: 40px;
            font-size: 14px;
        }
    </style>
</head>

<body>

<header>
    <img src="data:image/jpeg;base64,{{logo}}" alt="Logo zoeira">
    <h1>Kaik boca de 09</h1>
    <p>Site corporativo não oficial 😎</p>

    <nav>
        <a href="#home">Home</a>
        <a href="#sobre">Sobre</a>
        <a href="#servicos">Serviços</a>
        <a href="#contato">Contato</a>
    </nav>
</header>

<section class="banner" id="home">
    <h1>So presta pra morcegar</h1>
    <p>kkkkkkkkkkkkkkkkkkkk</p>
</section>

<section class="section" id="sobre">
    <h2>Quem Somos</h2>
    <p>
        A <strong>Kaik boca de 09</strong> é uma entidade misteriosa,
        especializada em dormir cedo, acordar tarde e
        entregar zero produtividade 😴🔥
    </p>
</section>

<section class="section" id="servicos">
    <h2>Nossos Serviços</h2>

    <div class="services">
        <div class="card">
            <h3>Especialista em Sumir</h3>
            <p>Promete aparecer, mas nunca chega.</p>
        </div>

        <div class="card">
            <h3>Consultoria em Soneca</h3>
            <p>Treinamento avançado em cochilos estratégicos.</p>
        </div>

        <div class="card">
            <h3>Fuga de Responsabilidade</h3>
            <p>Alta performance em escapar de tarefas.</p>
        </div>
    </div>
</section>

<section class="section" id="contato">
    <h2>Contato</h2>
    <p><strong>Email:</strong> nao_responde@kaik09.com</p>
    <p><strong>Telefone:</strong> Só chama se for pra zoar 😂</p>
</section>

<footer>
    © 2025 Kaik boca de 09 — Empresa 100% improdutiva
</footer>

</body>
</html>
"""

with open("logo.jpeg", "rb") as f:
    LOGO_BASE64 = base64.b64encode(f.read()).decode("utf-8")

@app.route("/")
def index():
    return render_template_string(HTML, logo=LOGO_BASE64)

if __name__ == "__main__":
    app.run(debug=True)
