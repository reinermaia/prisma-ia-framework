# language: pt
Funcionalidade: Verificação Automatizada de Requisitos de Segurança — PIX-GW

  Cenário: [SEC-REQ-01] Idempotência com assinatura mTLS legítima
    Dado que a ordem de liquidação possui certificado ICP-Brasil válido
    Quando o endpoint /api/v2/pix/settle processa o payload com hash SHA-256
    Então o serviço auth-broker-internal valida a chave pública
    E a transação é confirmada com status PAGO

  Cenário: [SEC-REQ-02] Bloqueio de Path Traversal CVE-2024-38816
    Dado que uma requisição externa contém caracteres '../' no cabeçalho ou URI
    Quando o Gateway intercepta o pacote HTTP
    Então a requisição é descartada com HTTP 400 Bad Request
