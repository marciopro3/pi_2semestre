## VIEW DE UNINDO TODAS AS INFORMAÇÕES QUE IMPORTAM PARA O POWER BI

CREATE VIEW `SBOReciclaSV`.`view_completa` AS
SELECT DISTINCT
    u.nome AS usuario_nome,
    u.email AS usuario_email,
    u.telefone AS usuario_telefone,
    u.dataCadastro AS usuario_dataCadastro,
    tu.tipo AS tipo_usuario,
    
    c.nome AS cidade_nome,
    
    d.nome AS deposito_nome,
    d.endereco AS deposito_endereco,
    d.cep AS deposito_cep,
    d.telefone AS deposito_telefone,
    d.capacidadeMaxima AS deposito_capacidadeMaxima,
    
    mat.nome AS material_nome,
    mat.descricao AS material_descricao,
    
    en.dataEntrada AS entrada_data,  -- Adicionando a data da entrada
     
    sa.dataSaida AS saida_data,
    sa.quantidade AS quantidade_saida,
    
    col.nome AS coletor_nome,
    col.cnpjCpf AS coletor_documento,
    col.telefone AS coletor_telefone,
    
    c2.nome AS coletor_cidade_nome,
    
    a.data AS agendamento_data,
    a.hora AS agendamento_hora,
    a.status AS agendamento_status

FROM 
    `SBOReciclaSV`.`usuario` u
INNER JOIN 
    `SBOReciclaSV`.`tipoUsuario` tu ON u.tipoUsuario_idtipoUsuario = tu.idtipoUsuario

INNER JOIN 
    `SBOReciclaSV`.`entrada` en ON u.idusuario = en.usuario_idusuario
INNER JOIN 
    `SBOReciclaSV`.`deposito` d ON en.deposito_iddeposito = d.iddeposito
INNER JOIN 
    `SBOReciclaSV`.`cidade` c ON d.cidade_idcidade = c.idcidade
INNER JOIN 
    `SBOReciclaSV`.`estado` e ON c.estado_idestado = e.idestado
INNER JOIN 
    `SBOReciclaSV`.`material` mat ON en.material_idmaterial = mat.idmaterial
INNER JOIN 
    `SBOReciclaSV`.`saida` sa ON d.iddeposito = sa.deposito_iddeposito
INNER JOIN 
    `SBOReciclaSV`.`coletor` col ON sa.coletor_idcoletor = col.idcoletor
INNER JOIN 
    `SBOReciclaSV`.`cidade` c2 ON col.cidade_idcidade = c2.idcidade
LEFT JOIN 
    `SBOReciclaSV`.`agendamento` a ON col.idcoletor = a.coletor_idcoletor;