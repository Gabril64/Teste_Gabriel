CREATE TABLE IF NOT EXISTS public.top10_operadoras_ultimo_ano
(
    registro_ans integer,
    razao_social text COLLATE pg_catalog."default",
    saldo_final_total numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.top10_operadoras_ultimo_ano
    OWNER to postgres;

COMMENT ON TABLE public.top10_operadoras_ultimo_ano
    IS 'Top 10 operadoras com maior saldo final acumulado no período de 01/10/2023 a 01/10/2024';
