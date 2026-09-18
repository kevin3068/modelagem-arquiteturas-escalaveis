import http from 'k6/http';
import { check, sleep } from 'k6';

const TOKEN = __ENV.MY_API_TOKEN;

export const options = {
    stages: [
        { duration: '10s', target: 50 },
        { duration: '30s', target: 100 }, // Força até 100 usuários
        { duration: '10s', target: 100 },
        { duration: '10s', target: 0 },
    ],
};

export default function () {
    const url = 'http://localhost:8000/api/dados-protegidos';
    const params = {
        headers: {
            'Authorization': `Bearer ${TOKEN}`,
            'Content-Type': 'application/json',
        },
    };

    const res = http.get(url, params);

    // Validações expandidas
    check(res, {
        'status foi 200': (r) => r.status === 200,
        'latência < 500ms': (r) => r.timings.duration < 500, // SLA alvo de meio segundo
        'resposta é JSON válido': (r) => {
            try { JSON.parse(r.body); return true; } catch { return false; }
        },
    });

    sleep(0.1);
}
