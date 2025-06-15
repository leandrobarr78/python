import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculadoraTurbo:
    def __init__(self, root):
        """Inicializa a calculadora com a janela principal"""
        self.root = root
        self.root.title("Calculadora Turbo 3.0")
        self.root.geometry("450x650")
        self.root.resizable(False, False)
        
        # Variáveis de controle
        self.entrada = tk.StringVar()  # Armazena o valor do display
        self.historico = []  # Armazena o histórico de cálculos
        self.memoria = None  # Armazena valores temporários
        
        # Configuração inicial
        self.configurar_estilos()
        self.criar_interface()
        self.criar_menu()

    def configurar_estilos(self):
        """Define os estilos visuais dos componentes"""
        style = ttk.Style()
        style.theme_use('clam')  # Tema moderno
        
        # Cores personalizadas
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TButton', font=('Arial', 14), padding=10)
        style.configure('Display.TEntry', font=('Arial', 28), foreground='#333')
        
        # Estilo dos botões especiais
        style.map('Operacao.TButton',
                 foreground=[('active', '#ffffff')],
                 background=[('active', '#4a6ea9')])
        style.map('Numero.TButton',
                 foreground=[('active', '#333333')],
                 background=[('active', '#e6e6e6')])

    def criar_interface(self):
        """Constrói todos os elementos da interface"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Display (área de visualização)
        display_frame = ttk.Frame(main_frame)
        display_frame.pack(fill=tk.X, pady=5)
        
        self.display = ttk.Entry(
            display_frame,
            textvariable=self.entrada,
            style='Display.TEntry',
            justify='right',
            state='readonly'
        )
        self.display.pack(fill=tk.X, ipady=15)
        
        # Frame do histórico
        historico_frame = ttk.Frame(main_frame)
        historico_frame.pack(fill=tk.X, pady=5)
        
        self.historico_label = ttk.Label(
            historico_frame,
            text="Histórico:",
            font=('Arial', 10),
            foreground='#666'
        )
        self.historico_label.pack(anchor='w')
        
        # Teclado numérico
        self.criar_teclado(main_frame)
        
        # Barra de status
        self.status = ttk.Label(
            main_frame,
            text="Pronto",
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status.pack(fill=tk.X, pady=(10,0))

    def criar_teclado(self, parent):
        """Cria os botões da calculadora"""
        teclado_frame = ttk.Frame(parent)
        teclado_frame.pack(fill=tk.BOTH, expand=True)
        
        # Layout do teclado (linha, coluna, texto, estilo, comando especial)
        botoes = [
            (0, 0, 'C', 'Operacao.TButton', self.limpar_tudo),
            (0, 1, '⌫', 'Operacao.TButton', self.apagar_ultimo),
            (0, 2, '%', 'Operacao.TButton', self.calcular_porcentagem),
            (0, 3, '√', 'Operacao.TButton', self.calcular_raiz),
            (1, 0, '7', 'Numero.TButton', None),
            (1, 1, '8', 'Numero.TButton', None),
            (1, 2, '9', 'Numero.TButton', None),
            (1, 3, '/', 'Operacao.TButton', None),
            (2, 0, '4', 'Numero.TButton', None),
            (2, 1, '5', 'Numero.TButton', None),
            (2, 2, '6', 'Numero.TButton', None),
            (2, 3, '*', 'Operacao.TButton', None),
            (3, 0, '1', 'Numero.TButton', None),
            (3, 1, '2', 'Numero.TButton', None),
            (3, 2, '3', 'Numero.TButton', None),
            (3, 3, '-', 'Operacao.TButton', None),
            (4, 0, '0', 'Numero.TButton', None),
            (4, 1, '.', 'Numero.TButton', None),
            (4, 2, '=', 'Operacao.TButton', self.calcular_resultado),
            (4, 3, '+', 'Operacao.TButton', None)
        ]
        
        # Cria os botões dinamicamente
        for (linha, coluna, texto, estilo, comando) in botoes:
            if comando is None:
                cmd = lambda t=texto: self.adicionar_entrada(t)
            else:
                cmd = comando
                
            btn = ttk.Button(
                teclado_frame,
                text=texto,
                style=estilo,
                command=cmd
            )
            btn.grid(
                row=linha,
                column=coluna,
                sticky='nsew',
                padx=2,
                pady=2,
                ipadx=5,
                ipady=5
            )
            teclado_frame.grid_columnconfigure(coluna, weight=1)
            teclado_frame.grid_rowconfigure(linha, weight=1)

    def criar_menu(self):
        """Cria o menu superior com funções avançadas"""
        menubar = tk.Menu(self.root)
        
        # Menu de operações
        menu_operacoes = tk.Menu(menubar, tearoff=0)
        menu_operacoes.add_command(
            label="Memória (M+)",
            command=self.adicionar_memoria
        )
        menu_operacoes.add_command(
            label="Recuperar Memória (MR)",
            command=self.recuperar_memoria
        )
        menu_operacoes.add_separator()
        menu_operacoes.add_command(
            label="Limpar Histórico",
            command=self.limpar_historico
        )
        menubar.add_cascade(label="Operações", menu=menu_operacoes)
        
        # Menu de porcentagem
        menu_porcent = tk.Menu(menubar, tearoff=0)
        menu_porcent.add_command(
            label="X% de Y",
            command=lambda: self.janela_porcentagem('x_de_y')
        )
        menu_porcent.add_command(
            label="X é % de Y",
            command=lambda: self.janela_porcentagem('x_eh_y')
        )
        menu_porcent.add_command(
            label="Aumentar X%",
            command=lambda: self.janela_porcentagem('aumentar')
        )
        menu_porcent.add_command(
            label="Reduzir X%",
            command=lambda: self.janela_porcentagem('reduzir')
        )
        menubar.add_cascade(label="Porcentagem", menu=menu_porcent)
        
        self.root.config(menu=menubar)

    # ============== FUNÇÕES PRINCIPAIS ==============
    def adicionar_entrada(self, valor):
        """Adiciona um caractere ao display"""
        atual = self.entrada.get()
        self.entrada.set(atual + valor)
        self.status.config(text="Entrada: " + self.entrada.get()[:20] + "...")

    def limpar_tudo(self):
        """Limpa completamente o display"""
        self.entrada.set('')
        self.status.config(text="Display limpo")

    def apagar_ultimo(self):
        """Remove o último caractere digitado"""
        atual = self.entrada.get()
        self.entrada.set(atual[:-1])
        self.status.config(text="Último caractere removido")

    def calcular_resultado(self):
        """Calcula a expressão matemática no display"""
        try:
            expressao = self.entrada.get()
            
            # Substitui símbolos para avaliação segura
            expressao = expressao.replace('×', '*').replace('÷', '/')
            
            # Cálculo seguro usando eval
            resultado = str(eval(expressao))
            
            # Atualiza histórico e display
            self.historico.append(f"{expressao} = {resultado}")
            self.entrada.set(resultado)
            self.status.config(text="Cálculo realizado")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Expressão inválida\n{str(e)}")
            self.status.config(text="Erro no cálculo")

    # ============== FUNÇÕES AVANÇADAS ==============
    def calcular_porcentagem(self):
        """Converte o valor atual para porcentagem"""
        try:
            valor = float(self.entrada.get())
            self.entrada.set(str(valor / 100))
            self.status.config(text="Convertido para porcentagem")
        except:
            messagebox.showerror("Erro", "Digite um número válido primeiro")

    def calcular_raiz(self):
        """Calcula a raiz quadrada do valor atual"""
        try:
            valor = float(self.entrada.get())
            if valor < 0:
                raise ValueError("Raiz de número negativo")
            self.entrada.set(str(math.sqrt(valor)))
            self.status.config(text="Raiz quadrada calculada")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            self.status.config(text="Erro ao calcular raiz")

    def adicionar_memoria(self):
        """Armazena o valor atual na memória"""
        try:
            self.memoria = float(self.entrada.get())
            self.status.config(text=f"Valor {self.memoria} armazenado na memória")
        except:
            messagebox.showerror("Erro", "Nada para armazenar na memória")

    def recuperar_memoria(self):
        """Recupera o valor da memória"""
        if self.memoria is not None:
            self.entrada.set(str(self.memoria))
            self.status.config(text="Valor recuperado da memória")
        else:
            messagebox.showinfo("Memória", "Nenhum valor armazenado")

    def limpar_historico(self):
        """Limpa todo o histórico de cálculos"""
        self.historico = []
        self.status.config(text="Histórico limpo")

    # ============== FUNÇÕES DE PORCENTAGEM ==============
    def janela_porcentagem(self, tipo):
        """Janela popup para cálculos complexos de porcentagem"""
        popup = tk.Toplevel(self.root)
        popup.title(tipo.replace('_', ' ').title())
        popup.geometry("300x250")
        popup.resizable(False, False)
        
        frame = ttk.Frame(popup)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Configuração dinâmica baseada no tipo de cálculo
        if tipo == 'x_de_y':
            ttk.Label(frame, text="Valor total (Y):").pack()
            entrada_y = ttk.Entry(frame)
            entrada_y.pack()
            
            ttk.Label(frame, text="Porcentagem (X%):").pack()
            entrada_x = ttk.Entry(frame)
            entrada_x.pack()
            
            def calcular():
                try:
                    y = float(entrada_y.get())
                    x = float(entrada_x.get())
                    resultado = y * (x / 100)
                    self.entrada.set(str(resultado))
                    popup.destroy()
                except ValueError:
                    messagebox.showerror("Erro", "Valores inválidos")
            
        elif tipo == 'x_eh_y':
            # Implementação similar para outros tipos
            pass
        
        # Botão de cálculo
        ttk.Button(
            frame,
            text="Calcular",
            command=calcular
        ).pack(pady=10)

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraTurbo(root)
    root.mainloop()