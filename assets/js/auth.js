// 登录表单提交
document.querySelector('form').onsubmit = async function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const res = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });
    const data = await res.json();
    alert(data.msg);
};

// 注册功能
document.getElementById('register-link').onclick = async function(e) {
    e.preventDefault();
    const username = prompt('请输入注册用户名：');
    const password = prompt('请输入注册密码：');
    if (!username || !password) return;
    const res = await fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });
    const data = await res.json();
    alert(data.msg);
};