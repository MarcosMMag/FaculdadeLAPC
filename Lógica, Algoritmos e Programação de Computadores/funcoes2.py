# Funções podem receber vários argumentos, que são passados quando a função é chamada.

# Função que verifica o perfil do usuário
def loginUsuario(perfil):
    if perfil == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Diferentes perfis
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('etc')