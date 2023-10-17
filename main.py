from futbolista import Futbolista
from deportista import Deportista
from persona import Persona

futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
ok = False
if (isinstance(futbolista, Deportista) and isinstance(futbolista, Persona)):
    ok = True


print(ok)