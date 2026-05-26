import Bladex
import ItemTypes 

print 'loading deaths...'


orlok_m10GuyInPieces0 = Bladex.CreateEntity('orlok_m10GuyInPieces0','Knight_Traitor',23002.5422579,-32949.2887635,59000.2035104,'Person')

orlok_m10GuyInPieces0.Angle = 2.3561925
orlok_m10GuyInPieces0.Life = 0
orlok_m10GuyInPieces0.SetOnFloor()

orlok_m10GuyInPieces1 = Bladex.CreateEntity('orlok_m10GuyInPieces1','Knight_Traitor',26502.5422698,-32949.2887635,58000.2035448,'Person')

orlok_m10GuyInPieces1.Angle = 3.14159
orlok_m10GuyInPieces1.Life = 0
orlok_m10GuyInPieces1.SetOnFloor()

Bladex.CreateEntity('BloodPool','Entity Pool',26510.3219165,-32000.0,57873.7678846)
Bladex.CreateEntity('BloodPool','Entity Pool',22922.5067581,-32000.0,58910.1330879)
Bladex.CreateEntity('BloodPool','Entity Pool',22937.8469784,-32000.0,58924.6268077)
Bladex.CreateEntity('BloodPool','Entity Pool',26509.4177843,-32000.0,57896.2888301)
Bladex.CreateEntity('BloodPool','Entity Pool',22946.5078481,-32000.0,58935.6679948)
Bladex.CreateEntity('BloodPool','Entity Pool',26508.9886086,-32000.0,57917.7401388)
Bladex.CreateEntity('BloodPool','Entity Pool',23103.4280716,-32000.0,59092.8447173)
Bladex.CreateEntity('BloodPool','Entity Pool',26507.832738,-32000.0,58139.590421)
Bladex.CreateEntity('BloodPool','Entity Pool',26506.9069965,-32000.0,57933.5593433)
Bladex.CreateEntity('BloodPool','Entity Pool',23143.2397729,-32000.0,59018.0233845)
Bladex.CreateEntity('BloodPool','Entity Pool',26580.4850955,-32000.0,58090.657565)
Bladex.CreateEntity('BloodPool','Entity Pool',23197.4427348,-32000.0,59483.4477395)
Bladex.CreateEntity('BloodPool','Entity Pool',26311.1811706,-32000.0,58443.2949679)
Bladex.CreateEntity('BloodPool','Entity Pool',22930.0260897,-32000.0,59843.0715614)
Bladex.CreateEntity('BloodPool','Entity Pool',25903.4890029,-32000.0,58489.5413969)
Bladex.CreateEntity('BloodPool','Entity Pool',22707.7853712,-32000.0,59756.3030986)
Bladex.CreateEntity('BloodPool','Entity Pool',25698.7646034,-32000.0,58376.1776637)
o = Bladex.CreateEntity('orlok_m10WeapDeath1','Espadaromana',26178.9559344,-32023.0173476,57592.6486998,'Weapon')
o.Orientation = 0.249661251903,0.286559700966,0.671525478363,-0.636086821556
ItemTypes.ItemDefaultFuncs(o)

Bladex.CreateEntity('BloodPool','Entity Pool',22437.2250634,-32000.0,59639.7930774)
Bladex.CreateEntity('BloodPool','Entity Pool',25665.1306972,-32000.0,58046.5307745)

o = orlok_m10GuyInPieces0.SeverLimb(1)
o.Stop()
o.Position    = 22953.229672,-32137.3635073,58940.2445187
o.Orientation = 0.99971562624,-0.0099125765264,-0.0169360488653,0.0135472789407

o = orlok_m10GuyInPieces1.SeverLimb(1)
o.Stop()
o.Position    = 26509.2056965,-32138.7048845,57916.3950134
o.Orientation = 0.999144971371,-0.00472019333392,-0.039264742285,0.0120563758537
o = Bladex.CreateEntity('orlok_m10WeapDeath0','CrushBo',22467.9484478,-32093.4625616,58881.3588456,'Weapon')
o.Orientation = 0.0748792514205,0.857273101807,-0.502034604549,-0.0862392783165
ItemTypes.ItemDefaultFuncs(o)

Bladex.CreateEntity('BloodPool','Entity Pool',22204.2794333,-32000.0,59605.1342945)
Bladex.CreateEntity('BloodPool','Entity Pool',25499.048335,-32000.0,57867.6954416)
Bladex.CreateEntity('BloodPool','Entity Pool',21906.3837828,-32000.0,59510.5901974)
Bladex.CreateEntity('BloodPool','Entity Pool',25475.5071504,-32000.0,57584.2334748)
Bladex.CreateEntity('BloodPool','Entity Pool',21597.0178771,-32000.0,59135.1011927)
Bladex.CreateEntity('BloodPool','Entity Pool',25406.6583903,-32000.0,57102.8888216)
Bladex.CreateEntity('BloodPool','Entity Pool',21202.4865573,-32000.0,58658.4139339)
Bladex.CreateEntity('BloodPool','Entity Pool',25451.513335,-32000.0,56469.134568)
Bladex.CreateEntity('BloodPool','Entity Pool',25732.1841281,-32000.0,55980.47036)
Bladex.CreateEntity('BloodPool','Entity Pool',21121.0361583,-32000.0,58145.3216635)
Bladex.CreateEntity('BloodPool','Entity Pool',21052.5705476,-32000.0,57679.6372926)
Bladex.CreateEntity('BloodPool','Entity Pool',26062.29141,-32000.0,55724.8412678)
