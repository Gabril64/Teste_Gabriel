CREATE TABLE IF NOT EXISTS public.top10_operadoras_trimestre
(
    registro_ans integer,
    razao_social text COLLATE pg_catalog."default",
    saldo_final_total numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.top10_operadoras_trimestre
    OWNER to postgres;

COMMENT ON TABLE public.top10_operadoras_trimestre
    IS 'Top 10 operadoras com maior saldo final no trimestre Jul-Set/2024';
