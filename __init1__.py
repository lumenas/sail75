# ...

config = Configurator(
    # ...
)
config.include('.models')
config.include('.routes')
config.include('.security')

config.add_route('login', '/login')
config.add_route('logout', '/logout')

# ...
