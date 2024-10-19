## TIPO USUÁRIO

USE sboreciclasv;

INSERT INTO tipousuario (idtipoUsuario, tipo) VALUES
(1, 'Cliente'),
(2, 'Funcionário'),
(3, 'Gerente'),
(4, 'Administrador'),
(5, 'Caixa'),
(6, 'Supervisor de Setor');

## USUÁRIO

INSERT INTO usuario (idusuario, nome, email, telefone, dataCadastro, tipoUsuario_idtipoUsuario) VALUES
(1, 'Carlos Silva', 'carlos.silva@email.com', '11987654321', '2020-03-15', 1),
(2, 'Maria Oliveira', 'maria.oliveira@email.com', '11987654322', '2021-06-22', 2),
(3, 'João Souza', 'joao.souza@email.com', '11987654323', '2022-09-10', 3),
(4, 'Ana Costa', 'ana.costa@email.com', '11987654324', '2023-01-08', 4),
(5, 'Paulo Ferreira', 'paulo.ferreira@email.com', '11987654325', '2019-07-20', 5),
(6, 'Cláudia Lima', 'claudia.lima@email.com', '11987654326', '2021-12-01', 6),
(7, 'Ricardo Alves', 'ricardo.alves@email.com', '11987654327', '2020-04-11', 1),
(8, 'Fernanda Martins', 'fernanda.martins@email.com', '11987654328', '2022-08-25', 2),
(9, 'Juliana Ribeiro', 'juliana.ribeiro@email.com', '11987654329', '2019-05-30', 3),
(10, 'Felipe Pinto', 'felipe.pinto@email.com', '11987654330', '2024-02-14', 4),
(11, 'Camila Barbosa', 'camila.barbosa@email.com', '11987654331', '2023-03-17', 5),
(12, 'Thiago Santos', 'thiago.santos@email.com', '11987654332', '2021-07-09', 6),
(13, 'Gabriel Rocha', 'gabriel.rocha@email.com', '11987654333', '2020-10-05', 1),
(14, 'Luciana Dias', 'luciana.dias@email.com', '11987654334', '2022-11-12', 2),
(15, 'Rodrigo Melo', 'rodrigo.melo@email.com', '11987654335', '2023-09-18', 3),
(16, 'Patrícia Cunha', 'patricia.cunha@email.com', '11987654336', '2019-04-24', 4),
(17, 'Renato Campos', 'renato.campos@email.com', '11987654337', '2020-02-06', 5),
(18, 'Débora Nunes', 'debora.nunes@email.com', '11987654338', '2021-05-27', 6),
(19, 'Sérgio Batista', 'sergio.batista@email.com', '11987654339', '2023-07-11', 1),
(20, 'Isabela Cardoso', 'isabela.cardoso@email.com', '11987654340', '2022-01-29', 2),
(21, 'Vitor Carvalho', 'vitor.carvalho@email.com', '11987654341', '2020-11-22', 3),
(22, 'Bianca Almeida', 'bianca.almeida@email.com', '11987654342', '2024-09-04', 4),
(23, 'André Matos', 'andre.matos@email.com', '11987654343', '2021-03-19', 5),
(24, 'Larissa Moura', 'larissa.moura@email.com', '11987654344', '2019-08-31', 6),
(25, 'Pedro Teixeira', 'pedro.teixeira@email.com', '11987654345', '2020-06-16', 1),
(26, 'Rafaela Monteiro', 'rafaela.monteiro@email.com', '11987654346', '2021-10-23', 2),
(27, 'Marcelo Gomes', 'marcelo.gomes@email.com', '11987654347', '2023-12-15', 3),
(28, 'Elaine Correia', 'elaine.correia@email.com', '11987654348', '2022-02-27', 4),
(29, 'Fábio Lopes', 'fabio.lopes@email.com', '11987654349', '2020-09-21', 5),
(30, 'Tatiane Azevedo', 'tatiane.azevedo@email.com', '11987654350', '2019-03-02', 6);

## CATEGORIA

INSERT INTO categoria (idcategoria, categoria) VALUES
(1, 'Papel'),
(2, 'Plástico'),
(3, 'Metal'),
(4, 'Vidro'),
(5, 'Tetra Pak'),
(6, 'Bateria');

## MATERIAL

INSERT INTO `SBOReciclaSV`.`material` (`idmaterial`, `nome`, `descricao`, `categoria_idcategoria`)
VALUES
(1, 'Papelão', 'Material de papel grosso usado em embalagens', 1),
(2, 'Garrafa PET', 'Garrafa de plástico transparente para bebidas', 2),
(3, 'Lata de Alumínio', 'Lata de bebida feita de alumínio', 3),
(4, 'Vidro Transparente', 'Vidro de garrafa sem cor', 4),
(5, 'Caixa Tetra Pak', 'Embalagem cartonada usada para sucos e leite', 5),
(6, 'Pilha AA', 'Bateria cilíndrica usada em pequenos aparelhos', 6),
(7, 'Papel Branco', 'Papel usado para impressão', 1),
(8, 'Saco Plástico', 'Saco utilizado para embalar produtos', 2),
(9, 'Lata de Aço', 'Lata utilizada para alimentos enlatados', 3),
(10, 'Vidro Colorido', 'Vidro de garrafa com cor', 4),
(11, 'Papelão Ondulado', 'Papelão com ondulações para maior resistência', 1),
(12, 'Embalagem de Plástico', 'Embalagem utilizada para alimentos', 2),
(13, 'Lata de Tinta', 'Lata usada para armazenamento de tinta', 3),
(14, 'Garrafão de Vidro', 'Garrafão utilizado para armazenar líquidos', 4),
(15, 'Caixa de Leite Tetra Pak', 'Embalagem para leite feita de Tetra Pak', 5),
(16, 'Bateria de Lítio', 'Bateria recarregável usada em dispositivos eletrônicos', 6),
(17, 'Papel Jornal', 'Papel utilizado para impressão de jornais', 1),
(18, 'Plástico Filme', 'Plástico fino utilizado para embalagens', 2),
(19, 'Fio de Cobre', 'Material utilizado para fiação elétrica', 3),
(20, 'Caco de Vidro', 'Pedaços de vidro quebrado', 4),
(21, 'Embalagem de Alumínio', 'Embalagem metálica utilizada para alimentos', 3),
(22, 'Papel Cartão', 'Papel mais grosso usado para cartões', 1),
(23, 'Tubo de PVC', 'Material plástico utilizado em encanamentos', 2),
(24, 'Lata de Spray', 'Lata usada para armazenar spray de tinta', 3),
(25, 'Garrafa de Vidro Verde', 'Garrafa feita de vidro verde', 4),
(26, 'Embalagem de Tetra Pak', 'Material composto de papel, plástico e alumínio', 5),
(27, 'Bateria de Carro', 'Bateria utilizada para automóveis', 6),
(28, 'Papel Manteiga', 'Papel usado em culinária', 1),
(29, 'Espuma Plástica', 'Material plástico leve e flexível', 2),
(30, 'Papel de Seda', 'Papel fino utilizado em embrulhos', 1);

## ESTADO

INSERT INTO estado (idestado, nome) VALUES
('AC', 'Acre'),
('AL', 'Alagoas'),
('AP', 'Amapá'),
('AM', 'Amazonas'),
('BA', 'Bahia'),
('CE', 'Ceará'),
('DF', 'Distrito Federal'),
('ES', 'Espírito Santo'),
('GO', 'Goiás'),
('MA', 'Maranhão'),
('MT', 'Mato Grosso'),
('MS', 'Mato Grosso do Sul'),
('MG', 'Minas Gerais'),
('PA', 'Pará'),
('PB', 'Paraíba'),
('PR', 'Paraná'),
('PE', 'Pernambuco'),
('PI', 'Piauí'),
('RJ', 'Rio de Janeiro'),
('RN', 'Rio Grande do Norte'),
('RS', 'Rio Grande do Sul'),
('RO', 'Rondônia'),
('RR', 'Roraima'),
('SC', 'Santa Catarina'),
('SP', 'São Paulo'),
('SE', 'Sergipe'),
('TO', 'Tocantins');

## CIDADE

INSERT INTO cidade (idcidade, nome, estado_idestado) VALUES
(1, 'Adamantina', 'SP'),
(2, 'Adolfo', 'SP'),
(3, 'Agudos', 'SP'),
(4, 'Alambari', 'SP'),
(5, 'Alfredo Marcondes', 'SP'),
(6, 'Altair', 'SP'),
(7, 'Altinópolis', 'SP'),
(8, 'Alumínio', 'SP'),
(9, 'Águas da Prata', 'SP'),
(10, 'Águas de Lindóia', 'SP'),
(11, 'Águas Virtuosas', 'SP'),
(12, 'Alegre', 'SP'),
(13, 'Aparecida', 'SP'),
(14, 'Araçariguama', 'SP'),
(15, 'Araçatuba', 'SP'),
(16, 'Araras', 'SP'),
(17, 'Arco-Íris', 'SP'),
(18, 'Areias', 'SP'),
(19, 'Arealva', 'SP'),
(20, 'Arujá', 'SP'),
(21, 'Aspásia', 'SP'),
(22, 'Atibaia', 'SP'),
(23, 'Auriflama', 'SP'),
(24, 'Bady Bassitt', 'SP'),
(25, 'Baldan', 'SP'),
(26, 'Bálsamo', 'SP'),
(27, 'Bananal', 'SP'),
(28, 'Barão de Antonina', 'SP'),
(29, 'Barbosa', 'SP'),
(30, 'Bariri', 'SP'),
(31, 'Barra Bonita', 'SP'),
(32, 'Barra do Chapéu', 'SP'),
(33, 'Barra do Turvo', 'SP'),
(34, 'Bastos', 'SP'),
(35, 'Bauru', 'SP'),
(36, 'Bebedouro', 'SP'),
(37, 'Bento de Abreu', 'SP'),
(38, 'Bernardino de Campos', 'SP'),
(39, 'Bertioga', 'SP'),
(40, 'Bilac', 'SP'),
(41, 'Birigui', 'SP'),
(42, 'Biritiba-Mirim', 'SP'),
(43, 'Boa Esperança do Sul', 'SP'),
(44, 'Bocaina', 'SP'),
(45, 'Bofete', 'SP'),
(46, 'Bonsucesso de Itararé', 'SP'),
(47, 'Borá', 'SP'),
(48, 'Boracéia', 'SP'),
(49, 'Borborema', 'SP'),
(50, 'Borebi', 'SP'),
(51, 'Botucatu', 'SP'),
(52, 'Bragança Paulista', 'SP'),
(53, 'Braúna', 'SP'),
(54, 'Brotas', 'SP'),
(55, 'Buritama', 'SP'),
(56, 'Buritizal', 'SP'),
(57, 'Cabrália Paulista', 'SP'),
(58, 'Cabreúva', 'SP'),
(59, 'Caconde', 'SP'),
(60, 'Cafelândia', 'SP'),
(61, 'Caiabu', 'SP'),
(62, 'Caieiras', 'SP'),
(63, 'Caiuá', 'SP'),
(64, 'Cajamar', 'SP'),
(65, 'Cajati', 'SP'),
(66, 'Cajuru', 'SP'),
(67, 'Campinas', 'SP'),
(68, 'Campo Limpo Paulista', 'SP'),
(69, 'Campo Novo do Sul', 'SP'),
(70, 'Cananéia', 'SP'),
(71, 'Canas', 'SP'),
(72, 'Cândido Mota', 'SP'),
(73, 'Cândido Rodrigues', 'SP'),
(74, 'Capão Bonito', 'SP'),
(75, 'Capela do Alto', 'SP'),
(76, 'Capivari', 'SP'),
(77, 'Caraguatatuba', 'SP'),
(78, 'Carapicuíba', 'SP'),
(79, 'Cardoso', 'SP'),
(80, 'Casa Branca', 'SP'),
(81, 'Cássia dos Coqueiros', 'SP'),
(82, 'Castilho', 'SP'),
(83, 'Catanduva', 'SP'),
(84, 'Catiguá', 'SP'),
(85, 'Cedral', 'SP'),
(86, 'Cerqueira César', 'SP'),
(87, 'Cerquilho', 'SP'),
(88, 'Charqueada', 'SP'),
(89, 'Chavantes', 'SP'),
(90, 'Clementina', 'SP'),
(91, 'Colina', 'SP'),
(92, 'Colômbia', 'SP'),
(93, 'Conchal', 'SP'),
(94, 'Conchas', 'SP'),
(95, 'Cordeirópolis', 'SP'),
(96, 'Corinthians', 'SP'),
(97, 'Coronel Macedo', 'SP'),
(98, 'Corumbataí', 'SP'),
(99, 'Cosmópolis', 'SP'),
(100, 'Cotia', 'SP'),
(101, 'Cravinhos', 'SP'),
(102, 'Cravinhos', 'SP'),
(103, 'Cruzália', 'SP'),
(104, 'Descalvado', 'SP'),
(105, 'Diadema', 'SP'),
(106, 'Dirce Reis', 'SP'),
(107, 'Divinolândia', 'SP'),
(108, 'Dobrada', 'SP'),
(109, 'Dolcinópolis', 'SP'),
(110, 'Dourado', 'SP'),
(111, 'Dracena', 'SP'),
(112, 'Duartina', 'SP'),
(113, 'Dumont', 'SP'),
(114, 'Echaporã', 'SP'),
(115, 'Eldorado', 'SP'),
(116, 'Elias Fausto', 'SP'),
(117, 'Elisiário', 'SP'),
(118, 'Embaú', 'SP'),
(119, 'Embu das Artes', 'SP'),
(120, 'Embu-Guaçu', 'SP'),
(121, 'Embu', 'SP'),
(122, 'Embu', 'SP'),
(123, 'Embu', 'SP'),
(124, 'Engenheiro Coelho', 'SP'),
(125, 'Espírito Santo do Pinhal', 'SP'),
(126, 'Estiva Gerbi', 'SP'),
(127, 'Fernandópolis', 'SP'),
(128, 'Fernão', 'SP'),
(129, 'Feliz Natal', 'SP'),
(130, 'Flora Rica', 'SP'),
(131, 'Floreal', 'SP'),
(132, 'Florínea', 'SP'),
(133, 'Franca', 'SP'),
(134, 'Francisco Morato', 'SP'),
(135, 'Franco da Rocha', 'SP'),
(136, 'Gabriel Monteiro', 'SP'),
(137, 'Gália', 'SP'),
(138, 'Garça', 'SP'),
(139, 'Gavion', 'SP'),
(140, 'General Salgado', 'SP'),
(141, 'Getulina', 'SP'),
(142, 'Glicério', 'SP'),
(143, 'Guaiçara', 'SP'),
(144, 'Guaraci', 'SP'),
(145, 'Guaranésia', 'SP'),
(146, 'Guarapiranga', 'SP'),
(147, 'Guaratinguetá', 'SP'),
(148, 'Guarulhos', 'SP'),
(149, 'Iacanga', 'SP'),
(150, 'Ibiúna', 'SP'),
(151, 'Ibitinga', 'SP'),
(152, 'Igarapava', 'SP'),
(153, 'Igaratá', 'SP'),
(154, 'Iguape', 'SP'),
(155, 'Ilha Comprida', 'SP'),
(156, 'Ilhabela', 'SP'),
(157, 'Indaiatuba', 'SP'),
(158, 'Inhaúma', 'SP'),
(159, 'Ipauçu', 'SP'),
(160, 'Iperó', 'SP'),
(161, 'Ipeúna', 'SP'),
(162, 'Ipiguá', 'SP'),
(163, 'Iporanga', 'SP'),
(164, 'Iracemápolis', 'SP'),
(165, 'Irapuru', 'SP'),
(166, 'Itaí', 'SP'),
(167, 'Itajubá', 'SP'),
(168, 'Itanhaém', 'SP'),
(169, 'Itapevi', 'SP'),
(170, 'Itapecerica da Serra', 'SP'),
(171, 'Itapetininga', 'SP'),
(172, 'Itapeva', 'SP'),
(173, 'Itapira', 'SP'),
(174, 'Itapirapuã Paulista', 'SP'),
(175, 'Itápolis', 'SP'),
(176, 'Itararé', 'SP'),
(177, 'Itatiba', 'SP'),
(178, 'Itaquaquecetuba', 'SP'),
(179, 'Itirapuã', 'SP'),
(180, 'Itobi', 'SP'),
(181, 'Itu', 'SP'),
(182, 'Itupeva', 'SP'),
(183, 'Jaborandi', 'SP'),
(184, 'Jaboticabal', 'SP'),
(185, 'Jacareí', 'SP'),
(186, 'Jaguariúna', 'SP'),
(187, 'Jales', 'SP'),
(188, 'Jambeiro', 'SP'),
(189, 'Jarinu', 'SP'),
(190, 'Jaú', 'SP'),
(191, 'Juliânia', 'SP'),
(192, 'Jundiaí', 'SP'),
(193, 'Junqueirópolis', 'SP'),
(194, 'Juquiá', 'SP'),
(195, 'Juquitiba', 'SP'),
(196, 'Lagoinha', 'SP'),
(197, 'Limeira', 'SP'),
(198, 'Lins', 'SP'),
(199, 'Lorena', 'SP'),
(200, 'Louvan', 'SP'),
(201, 'Louveira', 'SP'),
(202, 'Lucélia', 'SP'),
(203, 'Luís Antônio', 'SP'),
(204, 'Luiziânia', 'SP'),
(205, 'Macaubal', 'SP'),
(206, 'Mairiporã', 'SP'),
(207, 'Manduri', 'SP'),
(208, 'Marabá Paulista', 'SP'),
(209, 'Marília', 'SP'),
(210, 'Marinópolis', 'SP'),
(211, 'Mariporã', 'SP'),
(212, 'Mauá', 'SP'),
(213, 'Miracatu', 'SP'),
(214, 'Mirandópolis', 'SP'),
(215, 'Mogi das Cruzes', 'SP'),
(216, 'Mombuca', 'SP'),
(217, 'Monções', 'SP'),
(218, 'Monte Alegre do Sul', 'SP'),
(219, 'Monte Aprazível', 'SP'),
(220, 'Monte Mor', 'SP'),
(221, 'Morro Agudo', 'SP'),
(222, 'Murutinga do Sul', 'SP'),
(223, 'Nantes', 'SP'),
(224, 'Nazaré Paulista', 'SP'),
(225, 'Neves Paulista', 'SP'),
(226, 'Nhandeara', 'SP'),
(227, 'Nipoã', 'SP'),
(228, 'Nova Campina', 'SP'),
(229, 'Nova Canaã Paulista', 'SP'),
(230, 'Nova Odessa', 'SP'),
(231, 'Novais', 'SP'),
(232, 'Osasco', 'SP'),
(233, 'Ourinhos', 'SP'),
(234, 'Pacaembu', 'SP'),
(235, 'Padre Nóbrega', 'SP'),
(236, 'Palmital', 'SP'),
(237, 'Panorama', 'SP'),
(238, 'Paraguaçu Paulista', 'SP'),
(239, 'Paraibuna', 'SP'),
(240, 'Paranapanema', 'SP'),
(241, 'Paranavaí', 'SP'),
(242, 'Parapuã', 'SP'),
(243, 'Pardinho', 'SP'),
(244, 'Pariquera-Açu', 'SP'),
(245, 'Parisi', 'SP'),
(246, 'Patrocínio Paulista', 'SP'),
(247, 'Paulínia', 'SP'),
(248, 'Paulistânia', 'SP'),
(249, 'Pederneiras', 'SP'),
(250, 'Pedra Bela', 'SP'),
(251, 'Pedreira', 'SP'),
(252, 'Penápolis', 'SP'),
(253, 'Peruíbe', 'SP'),
(254, 'Piedade', 'SP'),
(255, 'Pindamonhangaba', 'SP'),
(256, 'Pindorama', 'SP'),
(257, 'Pinhalzinho', 'SP'),
(258, 'Piquete', 'SP'),
(259, 'Piracaia', 'SP'),
(260, 'Piracicaba', 'SP'),
(261, 'Piraju', 'SP'),
(262, 'Pirajuçara', 'SP'),
(263, 'Pitangueiras', 'SP'),
(264, 'Planalto', 'SP'),
(265, 'Planalto', 'SP'),
(266, 'Pocinhos do Sul', 'SP'),
(267, 'Pontal', 'SP'),
(268, 'Pontalinda', 'SP'),
(269, 'Porecatu', 'SP'),
(270, 'Porto Feliz', 'SP'),
(271, 'Porto Ferreira', 'SP'),
(272, 'Potim', 'SP'),
(273, 'Pracinha', 'SP'),
(274, 'Pradópolis', 'SP'),
(275, 'Prato', 'SP'),
(276, 'Presidente Alves', 'SP'),
(277, 'Presidente Bernardes', 'SP'),
(278, 'Presidente Epitácio', 'SP'),
(279, 'Presidente Prudente', 'SP'),
(280, 'Promissão', 'SP'),
(281, 'Quadra', 'SP'),
(282, 'Queimada', 'SP'),
(283, 'Queiroz', 'SP'),
(284, 'Rafard', 'SP'),
(285, 'Rancharia', 'SP'),
(286, 'Regente Feijó', 'SP'),
(287, 'Reginópolis', 'SP'),
(288, 'Ribeirão Bonito', 'SP'),
(289, 'Ribeirão Branco', 'SP'),
(290, 'Ribeirão Preto', 'SP'),
(291, 'Rocinha', 'SP'),
(292, 'Rochedo', 'SP'),
(293, 'Rosana', 'SP'),
(294, 'Roseira', 'SP'),
(295, 'Rubião Júnior', 'SP'),
(296, 'Sabino', 'SP'),
(297, 'Salgado de São Félix', 'SP'),
(298, 'Salto', 'SP'),
(299, 'Salto Grande', 'SP'),
(300, 'Santa Adélia', 'SP'),
(301, 'Santa Albertina', 'SP'),
(302, 'Santa Branca', 'SP'),
(303, 'Santa Clara do Sul', 'SP'),
(304, 'Santa Cruz das Palmeiras', 'SP'),
(305, 'Santa Cruz do Rio Pardo', 'SP'),
(306, 'Santa Ernestina', 'SP'),
(307, 'Santa Fé do Sul', 'SP'),
(308, 'Santa Gertrudes', 'SP'),
(309, 'Santa Isabel', 'SP'),
(310, 'Santa Rita do Passa Quatro', 'SP'),
(311, 'Santa Rosa de Viterbo', 'SP'),
(312, 'Santa Salete', 'SP'),
(313, 'Santo André', 'SP'),
(314, 'Santo Antônio da Alegria', 'SP'),
(315, 'Santo Antônio de Posse', 'SP'),
(316, 'Santo Antônio do Jardim', 'SP'),
(317, 'Santo Inácio', 'SP'),
(318, 'São Bento do Sapucaí', 'SP'),
(319, 'São Caetano do Sul', 'SP'),
(320, 'São Carlos', 'SP'),
(321, 'São Francisco', 'SP'),
(322, 'São João da Boa Vista', 'SP'),
(323, 'São João de Iracema', 'SP'),
(324, 'São José do Barreiro', 'SP'),
(325, 'São José dos Campos', 'SP'),
(326, 'São Lourenço da Serra', 'SP'),
(327, 'São Paulo', 'SP'),
(328, 'São Pedro', 'SP'),
(329, 'São Roque', 'SP'),
(330, 'São Sebastião', 'SP'),
(331, 'São Simão', 'SP'),
(332, 'São Vicente', 'SP'),
(333, 'Sarapuí', 'SP'),
(334, 'Sérgio', 'SP'),
(335, 'Sertãozinho', 'SP'),
(336, 'Sete Barras', 'SP'),
(337, 'Silveiras', 'SP'),
(338, 'Socorro', 'SP'),
(339, 'Sorocaba', 'SP'),
(340, 'Sud Mennucci', 'SP'),
(341, 'Sumaré', 'SP'),
(342, 'Suzano', 'SP'),
(343, 'Tabapuã', 'SP'),
(344, 'Tabatinga', 'SP'),
(345, 'Taiaçu', 'SP'),
(346, 'Tambaú', 'SP'),
(347, 'Tanabi', 'SP'),
(348, 'Tapiratiba', 'SP'),
(349, 'Tatuí', 'SP'),
(350, 'Tejupá', 'SP'),
(351, 'Teodoro Sampaio', 'SP'),
(352, 'Terra Roxa', 'SP'),
(353, 'Tietê', 'SP'),
(354, 'Torre de Pedra', 'SP'),
(355, 'Torrinha', 'SP'),
(356, 'Três Fronteiras', 'SP'),
(357, 'Tuiuti', 'SP'),
(358, 'Ubarana', 'SP'),
(359, 'Ubatuba', 'SP'),
(360, 'Ubirajara', 'SP'),
(361, 'Uchoa', 'SP'),
(362, 'Uniflor', 'SP'),
(363, 'Urânia', 'SP'),
(364, 'Urupês', 'SP'),
(365, 'Valentim Gentil', 'SP'),
(366, 'Valinhos', 'SP'),
(367, 'Vargem Grande do Sul', 'SP'),
(368, 'Vargem Grande Paulista', 'SP'),
(369, 'Várzea Paulista', 'SP'),
(370, 'Vera Cruz', 'SP'),
(371, 'Vinhedo', 'SP'),
(372, 'Viradouro', 'SP'),
(373, 'Vista Alegre do Alto', 'SP'),
(374, 'Votorantim', 'SP'),
(375, 'Votuporanga', 'SP'),
(376, 'Araraquara', 'SP');

## COLETOR

INSERT INTO coletor (idcoletor, nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro) VALUES
(1, 'ACME Indústria de Comércio de Lixo', '59.764.555/0001-52', '11987657294', 'Rua A, 123', 1, '2024-01-15'),
(2, 'Reciclável Soluções Ambientais', '12.345.678/0001-98', '11987654321', 'Rua B, 456', 2, '2024-02-10'),
(3, 'Green Future Coleta e Reciclagem', '34.567.890/0001-23', '11987651234', 'Avenida C, 789', 3, '2024-03-05'),
(4, 'Lixo Limpo Ltda.', '98.765.432/0001-11', '11987652345', 'Praça D, 147', 4, '2024-04-20'),
(5, 'Eco Coleta Ambiental', '87.654.321/0001-99', '11987653456', 'Rua E, 258', 5, '2024-05-25'),
(6, 'ReciclaBrasil', '56.789.012/0001-76', '11987654567', 'Avenida F, 369', 6, '2024-06-30'),
(7, 'Limpando o Futuro', '45.678.901/0001-55', '11987655678', 'Rua G, 852', 7, '2024-07-15'),
(8, 'Indústria Verde Coleta', '23.456.789/0001-44', '11987656789', 'Praça H, 963', 8, '2024-08-10'),
(9, 'Reciclagem Total', '67.890.123/0001-22', '11987657890', 'Rua I, 741', 9, '2024-09-05'),
(10, 'Coleta Ecológica', '78.901.234/0001-33', '11987658901', 'Avenida J, 258', 10, '2024-10-01'),
(11, 'Resíduos Sustentáveis', '89.012.345/0001-11', '11987659012', 'Rua K, 369', 11, '2024-11-20'),
(12, 'Indústria de Reciclagem Ecocycle', '90.123.456/0001-88', '11987660123', 'Praça L, 852', 12, '2024-12-15'),
(13, 'Lixo Verde Coleta', '21.234.567/0001-77', '11987661234', 'Rua M, 963', 13, '2024-01-05'),
(14, 'Reciclar é Viver', '32.345.678/0001-66', '11987662345', 'Avenida N, 147', 14, '2024-02-10'),
(15, 'Indústria de Coleta Ecológica', '43.456.789/0001-55', '11987663456', 'Rua O, 258', 15, '2024-03-25'),
(16, 'Verde e Limpo', '54.567.890/0001-44', '11987664567', 'Praça P, 369', 16, '2024-04-30'),
(17, 'Coleta Consciente', '65.678.901/0001-33', '11987665678', 'Rua Q, 852', 17, '2024-05-15'),
(18, 'Indústria Reciclagem Inteligente', '76.789.012/0001-22', '11987666789', 'Avenida R, 963', 18, '2024-06-05'),
(19, 'Coleta do Bem', '87.890.123/0001-11', '11987667890', 'Rua S, 741', 19, '2024-07-20'),
(20, 'ECO Lixo', '98.901.234/0001-99', '11987668901', 'Praça T, 258', 20, '2024-08-15'),
(21, 'Reciclagem e Sustentabilidade', '10.234.567/0001-88', '11987669012', 'Rua U, 369', 21, '2024-09-10'),
(22, 'Indústria de Coleta Sustentável', '21.345.678/0001-77', '11987670123', 'Avenida V, 852', 22, '2024-10-01'),
(23, 'Verde Coleta', '32.456.789/0001-66', '11987671234', 'Rua W, 963', 23, '2024-11-25'),
(24, 'Recicla Aí', '43.567.890/0001-55', '11987672345', 'Praça X, 147', 24, '2024-12-20'),
(25, 'Coletor Verde', '54.678.901/0001-44', '11987673456', 'Rua Y, 258', 25, '2024-01-10'),
(26, 'Indústria de Reciclagem Vida Verde', '65.789.012/0001-33', '11987674567', 'Avenida Z, 369', 26, '2024-02-05'),
(27, 'Reciclagem do Futuro', '76.890.123/0001-22', '11987675678', 'Rua AA, 852', 27, '2024-03-12'),
(28, 'Lixo e Cidadania', '87.901.234/0001-11', '11987676789', 'Praça AB, 963', 28, '2024-04-08'),
(29, 'Eco Coletor', '98.012.345/0001-99', '11987677890', 'Rua AC, 741', 29, '2024-05-25'),
(30, 'Indústria Reciclagem EcoBrasil', '10.123.456/0001-88', '11987678901', 'Praça AD, 258', 30, '2024-06-15');

## DEPÓSITO

INSERT INTO deposito (iddeposito, nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento) VALUES
(1, 'Mercearia São Rafael', 'R. Monsenhor João Ramalho, 777 - Jardim Nova Republica', '13875-249', 322, '1936313528', 5.000, '2024-09-25', '07:00:00', '21:00:00');

## AGENDAMENTO

INSERT INTO `SBOReciclaSV`.`agendamento` (`data`, `hora`, `status`, `coletor_idcoletor`)
VALUES
('2024-10-18', '08:30:00', 'Pendente', 1),
('2024-10-19', '14:00:00', 'Concluído', 2),
('2024-10-20', '09:15:00', 'Cancelado', 3),
('2024-10-21', '16:45:00', 'Pendente', 4),
('2024-10-22', '10:30:00', 'Concluído', 2),
('2024-10-23', '11:00:00', 'Pendente', 1),
('2024-10-24', '13:20:00', 'Concluído', 3),
('2024-10-25', '15:00:00', 'Pendente', 5),
('2024-10-26', '12:45:00', 'Cancelado', 4),
('2024-10-27', '07:30:00', 'Concluído', 2);

## ENTRADA

INSERT INTO entrada (identrada, usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade) VALUES
(1, 1, 1, 1, '2024-09-01', 0.80),
(2, 2, 1, 2, '2024-09-02', 1.50),
(3, 3, 1, 3, '2024-09-03', 2.00),
(4, 1, 1, 4, '2024-09-04', 3.25),
(5, 2, 1, 5, '2024-09-05', 0.50),
(6, 3, 1, 6, '2024-09-06', 1.20),
(7, 1, 1, 7, '2024-09-07', 4.10),
(8, 2, 1, 8, '2024-09-08', 0.90),
(9, 3, 1, 9, '2024-09-09', 1.75),
(10, 1, 1, 10, '2024-09-10', 2.50),
(11, 2, 1, 11, '2024-09-11', 0.60),
(12, 3, 1, 12, '2024-09-12', 3.00),
(13, 1, 1, 13, '2024-09-13', 2.80),
(14, 2, 1, 14, '2024-09-14', 1.00),
(15, 3, 1, 15, '2024-09-15', 5.00),
(16, 1, 1, 16, '2024-09-16', 0.30),
(17, 2, 1, 17, '2024-09-17', 1.50),
(18, 3, 1, 18, '2024-09-18', 0.75),
(19, 1, 1, 19, '2024-09-19', 4.20),
(20, 2, 1, 20, '2024-09-20', 0.85),
(21, 3, 1, 21, '2024-09-21', 2.10),
(22, 1, 1, 22, '2024-09-22', 1.45),
(23, 2, 1, 23, '2024-09-23', 3.65),
(24, 3, 1, 24, '2024-09-24', 0.95),
(25, 1, 1, 25, '2024-09-25', 2.25),
(26, 2, 1, 26, '2024-09-26', 1.15),
(27, 3, 1, 27, '2024-09-27', 3.80),
(28, 1, 1, 28, '2024-09-28', 0.55),
(29, 2, 1, 29, '2024-09-29', 1.05);

## SAIDA

INSERT INTO `SBOReciclaSV`.`saida` (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade)
VALUES
(1, 2, 1, '2024-10-01', 150.50),
(1, 3, 2, '2024-10-02', 200.75),
(1, 4, 3, '2024-10-03', 300.20),
(1, 5, 1, '2024-10-04', 400.60),
(1, 6, 2, '2024-10-05', 500.80),
(1, 7, 3, '2024-10-06', 250.30),
(1, 8, 4, '2024-10-07', 600.50),
(1, 9, 5, '2024-10-08', 100.90),
(1, 10, 6, '2024-10-09', 450.25),
(1, 11, 7, '2024-10-10', 700.40),
(1, 12, 8, '2024-10-11', 550.15),
(1, 13, 1, '2024-10-12', 350.75),
(1, 14, 2, '2024-10-13', 450.95),
(1, 15, 3, '2024-10-14', 320.35),
(1, 16, 4, '2024-10-15', 180.50),
(1, 17, 5, '2024-10-16', 590.10),
(1, 18, 6, '2024-10-17', 410.45),
(1, 19, 7, '2024-10-18', 270.80),
(1, 20, 8, '2024-10-19', 365.90),
(1, 21, 1, '2024-10-20', 430.20),
(1, 22, 2, '2024-10-21', 230.45),
(1, 23, 3, '2024-10-22', 320.15),
(1, 24, 4, '2024-10-23', 510.75),
(1, 25, 5, '2024-10-24', 290.40),
(1, 26, 6, '2024-10-25', 390.85),
(1, 27, 7, '2024-10-26', 420.95),
(1, 28, 8, '2024-10-27', 210.50),
(1, 29, 1, '2024-10-28', 310.30),
(1, 30, 2, '2024-10-29', 470.60),
(1, 1, 3, '2024-10-30', 190.25);