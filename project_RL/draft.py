import matplotlib.pyplot as plt

lis = [-49.8196748283246, -50.44799302251776, -50.44799302251776, -50.44799302251776, -50.44799302251776, -51.22499389946279, -50.44799302251776, -50.44799302251776, -50.44799302251776, -51.22499389946279, -51.22499389946279, -50.60632371551998, -49.20365840057018, -48.60041152089147, -48.60041152089147, -48.60041152089147, -48.60041152089147, -47.43416490252569, -46.87216658103186, -46.32493928760188, -46.87216658103186, -46.32493928760188, -45.79301256742124, -46.32493928760188, -46.32493928760188, -46.32493928760188, -47.43416490252569, -47.43416490252569, -48.010415536631214, -48.010415536631214, -48.60041152089147, -48.60041152089147, -48.60041152089147, -48.010415536631214, -48.60041152089147, -48.60041152089147, -49.20365840057018, -49.8196748283246, -49.8196748283246, -49.8196748283246, -49.8196748283246, -49.8196748283246, -49.20365840057018, -48.010415536631214, -48.60041152089147, -49.20365840057018, -48.60041152089147, -48.010415536631214, -49.20365840057018, -49.20365840057018, -48.60041152089147, -48.010415536631214, -48.010415536631214, -48.010415536631214, -47.43416490252569, -47.43416490252569, -47.43416490252569, -48.010415536631214, -47.43416490252569, -47.43416490252569, -46.87216658103186, -45.79301256742124, -45.27692569068709, -45.79301256742124, -45.79301256742124, -45.79301256742124, -46.32493928760188, -46.32493928760188, -46.32493928760188, -47.43416490252569, -47.43416490252569, -46.32493928760188, -44.77722635447622, -44.77722635447622, -45.27692569068709, -44.77722635447622, -44.77722635447622, -44.294469180700204, -44.294469180700204, -43.41658669218482, -42.941821107167776, -42.485291572496, -42.485291572496, -42.941821107167776, -45.27692569068709, -45.27692569068709, -45.79301256742124, -46.87216658103186, -47.43416490252569, -46.87216658103186, -46.87216658103186, -47.43416490252569, -47.43416490252569, -46.87216658103186, -46.87216658103186, -45.79301256742124, -45.27692569068709, -44.294469180700204, -44.77722635447622, -44.77722635447622, -42.485291572496, -42.485291572496, -42.485291572496, -42.04759208325728, -42.04759208325728, -42.04759208325728, -42.04759208325728, -42.04759208325728, -42.04759208325728, -42.04759208325728, -40.311288741492746, -40.718546143004666, -41.6293165929973, -41.6293165929973, -42.485291572496, -42.485291572496, -42.941821107167776, -42.04759208325728, -41.6293165929973, -42.485291572496, -42.941821107167776, -42.941821107167776, -42.941821107167776, -44.294469180700204, -44.294469180700204, -44.294469180700204, -44.294469180700204, -44.77722635447622, -44.294469180700204, -44.294469180700204, -44.294469180700204, -44.294469180700204, -44.294469180700204, -44.294469180700204, -44.77722635447622, -45.79301256742124, -45.79301256742124, -45.27692569068709, -45.27692569068709, -45.79301256742124, -45.79301256742124, -45.79301256742124, -45.79301256742124, -45.27692569068709, -45.27692569068709, -45.79301256742124, -45.27692569068709, -45.27692569068709, -45.27692569068709, -45.79301256742124, -45.27692569068709, -45.27692569068709, -44.77722635447622, -43.41658669218482, -43.41658669218482, -43.41658669218482, -44.77722635447622, -42.941821107167776, -42.941821107167776, -43.41658669218482, -44.294469180700204, -44.294469180700204, -43.41658669218482, -43.41658669218482, -43.41658669218482, -42.941821107167776, -42.04759208325728, -40.718546143004666, -40.718546143004666, -40.311288741492746, -39.92492955535426, -39.56008088970496, -39.56008088970496, -39.56008088970496, -39.56008088970496, -38.27531841800928, -37.94733192202055, -37.94733192202055, -37.94733192202055, -38.27531841800928, -38.27531841800928, -37.94733192202055, -37.64306044943742, -36.68787265568828, -36.68787265568828, -36.68787265568828, -37.64306044943742, -36.138621999185304, -35.90264614203248, -36.138621999185304, -36.40054944640259, -36.138621999185304, -35.90264614203248, -34.92849839314596, -34.713109915419565, -34.713109915419565, -34.713109915419565, -34.713109915419565, -34.713109915419565, -33.54101966249684, -38.27531841800928, -33.37663853655727, -31.016124838541646, -31.064449134018133, -31.144823004794873, -31.064449134018133, -31.064449134018133, -30.01666203960727, -30.01666203960727, -30.01666203960727, -31.064449134018133, -31.016124838541646, -30.0, -30.0, -30.0, -30.0, -30.01666203960727, -30.01666203960727, -30.01666203960727, -31.016124838541646, -31.064449134018133, -32.2490309931942, -33.24154027718932, -32.14031735997639, -31.064449134018133, -31.016124838541646, -30.01666203960727, -30.01666203960727, -30.01666203960727, -30.01666203960727, -30.0, -29.0, -30.0, -30.01666203960727, -30.01666203960727, -30.01666203960727, -30.01666203960727, -29.0, -29.0, -29.0, -29.017236257093817, -29.0, -30.01666203960727, -31.064449134018133, -31.064449134018133, -32.14031735997639, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.14031735997639, -32.14031735997639, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.14031735997639, -32.14031735997639, -32.14031735997639, -32.14031735997639, -32.14031735997639, -32.2490309931942, -33.54101966249684, -34.92849839314596, -36.138621999185304, -36.138621999185304, -36.138621999185304, -36.138621999185304, -35.90264614203248, -35.90264614203248, -35.90264614203248, -34.713109915419565, -34.52535300326414, -34.713109915419565, -34.713109915419565, -34.92849839314596, -36.40054944640259, -36.40054944640259, -36.40054944640259, -37.64306044943742, -37.64306044943742, -37.64306044943742, -37.36308338453881, -37.94733192202055, -37.94733192202055, -38.27531841800928, -39.21734310225516, -37.94733192202055, -37.94733192202055, -37.64306044943742, -36.40054944640259, -36.138621999185304, -35.90264614203248, -35.90264614203248, -36.138621999185304, -36.138621999185304, -36.138621999185304, -36.40054944640259, -34.92849839314596, -33.54101966249684, -33.54101966249684, -34.713109915419565, -34.92849839314596, -34.713109915419565, -34.713109915419565, -36.138621999185304, -37.64306044943742, -37.94733192202055, -39.21734310225516, -39.21734310225516, -38.27531841800928, -37.94733192202055, -37.94733192202055, -37.64306044943742, -37.36308338453881, -36.40054944640259, -37.36308338453881, -36.40054944640259, -36.40054944640259, -37.64306044943742, -37.94733192202055, -39.21734310225516, -39.21734310225516, -37.94733192202055, -37.94733192202055, -37.94733192202055, -37.94733192202055, -37.94733192202055, -37.64306044943742, -36.40054944640259, -36.40054944640259, -36.40054944640259, -36.138621999185304, -34.92849839314596, -33.54101966249684, -33.37663853655727, -32.2490309931942, -31.144823004794873, -32.14031735997639, -32.2490309931942, -32.14031735997639, -32.2490309931942, -33.37663853655727, -33.54101966249684, -33.37663853655727, -33.37663853655727, -33.37663853655727, -33.54101966249684, -34.713109915419565, -34.713109915419565, -33.54101966249684, -32.2490309931942, -32.2490309931942, -32.2490309931942, -32.38826948140329, -32.38826948140329, -33.54101966249684, -33.734255586866, -34.713109915419565, -34.92849839314596, -35.17101079013795, -34.92849839314596, -34.713109915419565, -33.734255586866, -33.734255586866, -34.713109915419565, -34.713109915419565, -34.92849839314596, -34.713109915419565, -34.713109915419565, -33.734255586866, -33.734255586866, -34.713109915419565, -34.713109915419565, -34.92849839314596, -34.92849839314596, -34.92849839314596, -33.734255586866, -33.734255586866, -33.734255586866, -32.38826948140329, -32.38826948140329, -33.54101966249684, -33.54101966249684, -32.38826948140329, -33.734255586866, -33.734255586866, -33.734255586866, -33.54101966249684, -33.54101966249684, -32.38826948140329, -32.55764119219941, -32.55764119219941, -33.54101966249684, -32.55764119219941, -33.54101966249684, -34.92849839314596, -34.92849839314596, -32.38826948140329, -32.38826948140329, -32.55764119219941, -32.38826948140329, -32.38826948140329, -31.400636936215164, -31.25699921617557, -31.400636936215164, -31.400636936215164, -32.38826948140329, -31.400636936215164, -31.25699921617557, -31.25699921617557, -32.38826948140329, -32.55764119219941, -32.38826948140329, -31.25699921617557, -31.25699921617557, -31.25699921617557, -30.265491900843113, -31.400636936215164, -31.400636936215164, -31.400636936215164, -31.575306807693888, -31.400636936215164, -31.400636936215164, -30.4138126514911, -31.400636936215164, -31.400636936215164, -31.400636936215164, -31.575306807693888, -31.575306807693888, -31.575306807693888, -31.575306807693888, -31.575306807693888, -31.575306807693888, -32.7566787083184, -32.7566787083184, -32.7566787083184, -33.95585369269929, -33.95585369269929, -32.7566787083184, -31.575306807693888, -31.400636936215164, -30.4138126514911, -30.265491900843113, -31.400636936215164, -31.400636936215164, -31.400636936215164, -31.400636936215164, -31.400636936215164, -31.400636936215164, -31.400636936215164, -30.265491900843113, -29.154759474226502, -29.154759474226502, -29.068883707497267, -28.071337695236398, -28.071337695236398, -28.160255680657446, -29.274562336608895, -30.265491900843113, -30.265491900843113, -29.154759474226502, -29.154759474226502, -29.154759474226502, -29.068883707497267, -29.154759474226502, -29.154759474226502, -29.154759474226502, -30.14962686336267, -31.25699921617557, -31.25699921617557, -31.25699921617557, -31.25699921617557, -30.265491900843113, -30.14962686336267, -30.14962686336267, -30.14962686336267, -29.068883707497267, -29.068883707497267, -29.068883707497267, -29.154759474226502, -29.068883707497267, -28.071337695236398, -28.071337695236398, -28.0178514522438, -27.018512172212592, -26.0, -27.0, -28.0178514522438, -28.071337695236398, -29.068883707497267, -30.14962686336267, -30.066592756745816, -29.068883707497267, -30.14962686336267, -30.066592756745816, -30.14962686336267]

plt.plot(lis)
episode = 10
file_name = './img' + str(episode) + '.png'
plt.savefig(file_name)
# plt.close()
# plt.show()