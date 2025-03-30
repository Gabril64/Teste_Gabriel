CREATE TABLE relatorio_unificado AS
SELECT 
    rc.*,
    cc.data as data_conta,
    cc.cd_conta_contabil,
    cc.descricao,
    cc.vl_saldo_inicial,
    cc.vl_saldo_final
FROM 
    relatorio_cadop rc
LEFT JOIN 
    contas_cobrancas cc ON rc.registro_ans = cc.reg_ans::integer
    AND cc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR  ';

