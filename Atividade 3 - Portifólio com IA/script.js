// 1. Seleciona o botão e o elemento <body>
const themeToggleBtn = document.getElementById('theme-toggle');
const bodyElement = document.body;

// 2. Adiciona um 'ouvinte de eventos' que detecta quando o botão é clicado
themeToggleBtn.addEventListener('click', () => {
    // 3. Alterna (liga/desliga) a classe 'dark-mode' no <body>
    bodyElement.classList.toggle('dark-mode');
    
    // 4. Muda o texto do botão dependendo do modo atual
    if (bodyElement.classList.contains('dark-mode')) {
        themeToggleBtn.textContent = '☀️ Modo Claro';
    } else {
        themeToggleBtn.textContent = '🌙 Modo Escuro';
    }
});