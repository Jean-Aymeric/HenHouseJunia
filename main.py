from behaviorsing.behaviorsing import BehaviorSing
from behaviorsing.behaviorsingcotcotcon import BehaviorSingCotCotCon
from gasconhen import GasconHen
from gingerhen import GingerHen
from henhouse import Henhouse
from plastichen import PlasticHen


henhouse = Henhouse()
hen1 = GingerHen("Gilberte", "Gigi")
hen2 = GingerHen("Gilberto")
hen3 = GasconHen("Dartagnan", "Darti")
hen4= PlasticHen("Jo")

henhouse.addHen(hen1)
henhouse.addHen(hen2)
henhouse.addHen(hen3)
henhouse.addHen(hen4)

henhouse.singAll()

hen4.setBehaviorSing(BehaviorSingCotCotCon())
hen2.setBehaviorSing(hen3.getBehaviorSing())

henhouse.singAll()

hen3.setBehaviorSing(hen1.getBehaviorSing())

henhouse.singAll()
hen4.setBehaviorSing(BehaviorSing())
