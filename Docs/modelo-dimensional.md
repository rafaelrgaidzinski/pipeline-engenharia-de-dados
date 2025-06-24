---
hide:
  - navigation
---

# Modelo Dimensional

---

> Abaixo está o diagrama representando as tabelas fato e suas dimensões:

![Modelo Dimensional](Images/modelo_dimensional.png)

## Fato: `fact_orders`

Armazena informações de pedidos realizados, incluindo quantidades de itens, status de entrega, valores totais e dados de aprovação.

### Principais atributos:
- `items_count`: quantidade de itens no pedido
- `is_delivered`: flag indicando se o pedido foi entregue
- `is_delivered_on_time`: flag indicando se a entrega foi no prazo
- `total_freight`: valor total do frete
- `total_price`: valor total dos produtos
- `total_payment`: valor total pago
- `is_approved`: flag indicando se o pedido foi aprovado
- `order_year` e `order_month`: extraídos da data de aprovação
- `main_payment_type`: principal forma de pagamento utilizada
- `customer_city` e `customer_state`: localização do cliente

---

## Dimensões

### `dim_orders`

Contém detalhes do pedido como status, data de aprovação, entrega e previsão de entrega.

### `dim_customer`

Contém dados dos clientes como cidade e estado.

### `dim_order_items`

Detalha os itens de cada pedido, incluindo preço e valor de frete por item.

### `dim_order_payments`

Armazena as informações de pagamento por pedido, incluindo valor e tipo de pagamento.

### `dim_payment_types`

Lista os tipos de pagamento disponíveis (e.g., cartão de crédito, boleto, etc.).

---

Este modelo permite as seguintes análises:

KPIs 

-> Taxa de entregas no prazo <br>
-> Frete médio por pedido <br>
-> Ticket médio por pedido <br>
-> Taxa de aprovação de pedido

Métricas

-> Distribuição dos tipos de pagamento <br>
-> Cidades dos cliente que mais compraram
