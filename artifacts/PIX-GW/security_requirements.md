# Catálogo de Requisitos de Segurança Formais — PIX-GW

> Derivado formalmente a partir do Relatório de Modelagem de Ameaças (STRIDE)
> Padrão: OWASP Application Security Verification Standard (ASVS) 4.0.3 + BDD Gherkin

## Sumário
- **Projeto:** PIX-GW
- **Total de Requisitos Derivados:** 3
- **Rastreabilidade Bidirecional:** 100% de cobertura das ameaças STRIDE

---

### [SEC-REQ-01] Não-Repúdio e Idempotência de Transação via mTLS e Assinatura ECDSA
- **Ameaças Mitigadas:** `THREAT-01, THREAT-04`
- **Capítulo ASVS:** `V3.2 (Session Management & Cryptography)` (Nível 3 (Software Crítico))
- **Critérios INVEST:** Independente, Negociável, Valioso, Estimável, Sucinto, Testável (INVEST Validado)
- **Especificação Técnica:**
  O gateway de liquidação deve validar a assinatura digital ECDSA secp256r1 com hash SHA-256 no cabeçalho da requisição e impor janela de idempotência de 300 segundos via Redis Cluster antes de processar qualquer liquidação financeira.

#### Cenários de Teste de Aceitação (BDD Gherkin):
```gherkin
Funcionalidade: Validação de Idempotência e Autenticidade Pix
  Cenário: Liquidação legítima com assinatura válida
    Dado que uma ordem de pagamento é enviada com certificado ICP-Brasil válido
    Quando o endpoint /api/v2/pix/settle recebe a carga útil com hash SHA-256
    Então o serviço auth-broker-internal confirma a chave pública
    E a transação é registrada no ledger contábil com status PAGO

  Cenário: Reutilização de token (Replay Attack)
    Dado que um hash de transação já foi processado nos últimos 300 segundos
    Quando a mesma requisição for submetida novamente
    Então o Gateway deve responder HTTP 409 Conflict com mensagem 'IDEMPOTENCY_KEY_REUSED'
    E disparar alerta de segurança para o SIEM corporativo
```

---
### [SEC-REQ-02] Filtro Sanitizador de Traversal e Isolamento de Functional Endpoints
- **Ameaças Mitigadas:** `THREAT-03`
- **Capítulo ASVS:** `V5.1 (Input Validation & Framework Security)` (Nível 2)
- **Critérios INVEST:** INVEST Validado
- **Especificação Técnica:**
  O Router HTTP deve aplicar expressão regular canônica e normalização de caminho UTF-8 em todos os headers e URIs antes de despachar a rota, bloqueando sequências '../' ou '..%2f' para neutralizar o exploit CVE-2024-38816.

#### Cenários de Teste de Aceitação (BDD Gherkin):
```gherkin
Funcionalidade: Mitigação de Path Traversal no Router
  Cenário: Tentativa de travessia de diretório em endpoint público
    Dado que um atacante envia uma requisição com caracteres '../' na URI
    Quando a camada de filtro do API Gateway intercepta a chamada
    Então o pacote deve ser imediatamente descartado com HTTP 400 Bad Request
    E a conexão TCP deve ser finalizada sem expor stacktrace
```

---
### [SEC-REQ-03] Parametrização Estrita de Consultas SQL no Módulo Ledger
- **Ameaças Mitigadas:** `THREAT-02`
- **Capítulo ASVS:** `V5.3 (Output Encoding & SQL Injection Prevention)` (Nível 2)
- **Critérios INVEST:** INVEST Validado
- **Especificação Técnica:**
  Todas as operações no repositório ledger_dao.go devem utilizar obrigatoriamente Prepared Statements nativos do driver SQL, sendo terminantemente proibida a concatenação dinâmica de strings.

#### Cenários de Teste de Aceitação (BDD Gherkin):
```gherkin
Funcionalidade: Prevenção de SQL Injection no Conciliador
  Cenário: Tentativa de injeção em filtro de data ou transação
    Dado que um payload contém caracteres como '' OR 1=1 --'
    Quando a query de consulta de extrato for compilada
    Então o parâmetro deve ser tratado estritamente como string literal
    E nenhuma sintaxe SQL injetada deve ser executada pelo banco de dados
```

---
