from launcher import Launcher

if __name__ == "__main__":
    Launchers = Launcher()
    lg = Launchers.iniciarLogin()
    if lg.afiliacion[0] == "aeropuerto el campanero":
        Launchers.iniciarAdministrador(lg.name)
    else:
        Launchers.iniciarFunAerolinea(lg.afiliacion[0], lg.name)
  