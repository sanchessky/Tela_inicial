# Projeto de Tela de Venda
# @author Thiago Sanches
# @author Lucas Henrique
# @author Allan Vítor

# Importar as bibliotecas do PyQt5
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
)
import sys

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar a geometria da tela (posição X e Y, largura e altura)
        self.setGeometry(500, 30, 648, 408)
        self.setWindowTitle("Caixa")

        # Layout principal vertical
        self.layout_v_total = QVBoxLayout()

    

        # ========================== Título =============================
        self.label_titulo = QLabel("Finalizar Venda")
        self.label_titulo.setStyleSheet("QLabel{background-color:white; font-size: 14px; font-weight: bold; padding: 5px;}")
        self.label_titulo.setFixedHeight(70)  
        self.layout_v_total.addWidget(self.label_titulo)
        # ======================== Fim do Título =========================

        # ========================== Dados ==============================
        self.label_dados = QLabel()
        self.layout_h_dados = QHBoxLayout()

        # ==================== Coluna Esquerda ==========================
        self.label_esquerda = QLabel()
        self.layout_v_esquerda = QVBoxLayout()

        # ======== Total de Venda ========
        self.layout_h_total_venda = QHBoxLayout()
        self.label_venda = QLabel("Total de Venda")
        self.edit_venda = QLineEdit("R$ 0,00")
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)
        self.layout_v_esquerda.addLayout(self.layout_h_total_venda)

        # ========= Desconto =========
        self.layout_h_desconto = QHBoxLayout()
        self.label_desc = QLabel("Desconto:")
        self.edit_desc = QLineEdit("R$ 0,00")
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)
        self.layout_v_esquerda.addLayout(self.layout_h_desconto)

        # ========= Acréscimo =========
        self.layout_h_acrecimo = QHBoxLayout()
        self.label_acre = QLabel("Acréscimo:")
        self.edit_acre = QLineEdit("R$ 0,00")
        self.layout_h_acrecimo.addWidget(self.label_acre)
        self.layout_h_acrecimo.addWidget(self.edit_acre)
        self.layout_v_esquerda.addLayout(self.layout_h_acrecimo)

        # ========= Total Líquido =========
        self.layout_h_total_liquido = QHBoxLayout()
        self.label_liquido = QLabel("Total Líquido:")
        self.edit_liquido = QLineEdit("R$ 0,00")
        self.layout_h_total_liquido.addWidget(self.label_liquido)
        self.layout_h_total_liquido.addWidget(self.edit_liquido)
        self.layout_v_esquerda.addLayout(self.layout_h_total_liquido)

        # ========= Troco =========
        self.layout_h_total_troco = QHBoxLayout()
        self.label_troco = QLabel("Total Troco:")
        self.edit_troco = QLineEdit("R$ 0,00")
        self.layout_h_total_troco.addWidget(self.label_troco)
        self.layout_h_total_troco.addWidget(self.edit_troco)
        self.layout_v_esquerda.addLayout(self.layout_h_total_troco)

        self.label_esquerda.setLayout(self.layout_v_esquerda)
        self.layout_h_dados.addWidget(self.label_esquerda)

        # ==================== Coluna Direita ==========================
        self.label_direita = QLabel()
        self.layout_v_direita = QVBoxLayout()

        # ======== Cliente ========
        self.layout_h_cliente = QHBoxLayout()
        self.label_cliente = QLabel("Cliente:")
        self.edit_cliente = QLineEdit(" ")
        self.layout_h_cliente.addWidget(self.label_cliente)
        self.layout_h_cliente.addWidget(self.edit_cliente)
        self.layout_v_direita.addLayout(self.layout_h_cliente)

        # ======== Vendedor ========
        self.layout_h_vendedor = QHBoxLayout()
        self.label_vendedor = QLabel("Vendedor:")
        self.edit_vendedor = QLineEdit(" ")
        self.layout_h_vendedor.addWidget(self.label_vendedor)
        self.layout_h_vendedor.addWidget(self.edit_vendedor)
        self.layout_v_direita.addLayout(self.layout_h_vendedor)

        # ======== Forma de Pagamento ========
        self.layout_h_pagamento = QHBoxLayout()
        self.label_pagamento = QLabel("Forma de Pagamento:")
        self.combo_pagamento = QComboBox()
        self.combo_pagamento.addItems(["DINHEIRO", "CARTÃO", "PIX"])
        self.layout_h_pagamento.addWidget(self.label_pagamento)
        self.layout_h_pagamento.addWidget(self.combo_pagamento)
        self.layout_v_direita.addLayout(self.layout_h_pagamento)

        self.label_direita.setLayout(self.layout_v_direita)
        self.layout_h_dados.addWidget(self.label_direita)

        self.label_dados.setLayout(self.layout_h_dados)
        self.layout_v_total.addWidget(self.label_dados)
        # ======================== Fim dos Dados =========================

        # ========================== Rodapé =============================
        self.label_rodape = QLabel()
        self.layout_h_botoes = QHBoxLayout()

        self.btn_cupom = QPushButton("(F6) Cupom Fiscal")
        self.btn_pedido = QPushButton("(F7) Pedido de Venda")
        self.btn_nfc_online = QPushButton("(F8) NFC-e OnLine")
        self.btn_nfc_offline = QPushButton("(F9) NFC-e OffLine")
        self.btn_sair = QPushButton("(Esc) Sair")

        self.layout_h_botoes.addWidget(self.btn_cupom)
        self.layout_h_botoes.addWidget(self.btn_pedido)
        self.layout_h_botoes.addWidget(self.btn_nfc_online)
        self.layout_h_botoes.addWidget(self.btn_nfc_offline)
        self.layout_h_botoes.addWidget(self.btn_sair)

        self.label_rodape.setLayout(self.layout_h_botoes)
        self.layout_v_total.addWidget(self.label_rodape)
        # ======================== Fim do Rodapé =========================

        # Definir o layout principal
        self.setLayout(self.layout_v_total)

# ========================== Execução =============================
app = QApplication(sys.argv)
tela = CaixaMercado()
tela.show()
app.exec()
