CREATE VIEW SBOReciclaSV.vw_completa AS
SELECT
    u.idusuario AS UsuarioID,
    u.nome AS UsuarioNome,
    u.email AS UsuarioEmail,
    u.telefone AS UsuarioTelefone,
    u.dataCadastro AS UsuarioDataCadastro,
    tu.tipo AS TipoUsuario,
    c.nome AS ColetorNome,
    c.cnpjCpf AS ColetorCnpjCpf,
    c.telefone AS ColetorTelefone,
    c.endereco AS ColetorEndereco,
    cid_c.nome AS ColetorCidade,
    est_c.nome AS ColetorEstado,
    a.idagendamento AS AgendamentoID,
    a.data AS AgendamentoData,
    a.hora AS AgendamentoHora,
    a.status AS AgendamentoStatus,
    m.nome AS MaterialNome,
    m.descricao AS MaterialDescricao,
    cat.categoria AS CategoriaMaterial,
    dep.nome AS DepositoNome,
    dep.endereco AS DepositoEndereco,
    dep.cep AS DepositoCEP,
    cid_d.nome AS DepositoCidade,
    est_d.nome AS DepositoEstado,
    dep.telefone AS DepositoTelefone,
    dep.capacidadeMaxima AS DepositoCapacidadeMaxima,
    dep.dataCadastro AS DepositoDataCadastro,
    e.identrada AS EntradaID,
    e.dataEntrada AS EntradaData,
    e.quantidade AS EntradaQuantidade,
    s.idsaida AS SaidaID,
    s.dataSaida AS SaidaData,
    s.quantidade AS SaidaQuantidade
FROM
    SBOReciclaSV.usuario u
    INNER JOIN SBOReciclaSV.tipoUsuario tu ON u.tipoUsuario_idtipoUsuario = tu.idtipoUsuario
    LEFT JOIN SBOReciclaSV.entrada e ON u.idusuario = e.usuario_idusuario
    LEFT JOIN SBOReciclaSV.material m ON e.material_idmaterial = m.idmaterial
    LEFT JOIN SBOReciclaSV.categoria cat ON m.categoria_idcategoria = cat.idcategoria
    LEFT JOIN SBOReciclaSV.deposito dep ON e.deposito_iddeposito = dep.iddeposito
    LEFT JOIN SBOReciclaSV.cidade cid_d ON dep.cidade_idcidade = cid_d.idcidade
    LEFT JOIN SBOReciclaSV.estado est_d ON cid_d.estado_idestado = est_d.idestado
    LEFT JOIN SBOReciclaSV.saida s ON s.coletor_idcoletor = e.usuario_idusuario
    LEFT JOIN SBOReciclaSV.coletor c ON s.coletor_idcoletor = c.idcoletor
    LEFT JOIN SBOReciclaSV.cidade cid_c ON c.cidade_idcidade = cid_c.idcidade
    LEFT JOIN SBOReciclaSV.estado est_c ON cid_c.estado_idestado = est_c.idestado
    LEFT JOIN SBOReciclaSV.agendamento a ON a.coletor_idcoletor = c.idcoletor;