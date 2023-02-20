import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import polyfit, poly1d

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
diffi = [4.11908, 4.56098, 4.66002, 4.40617, 4.43884, 4.33798, 4.39121, 4.34075, 4.28977, 4.50703, 4.33675, 4.52865, 4.23395, 4.40224, 4.3546, 4.37765, 4.64952, 4.5414, 4.38449, 4.46543, 4.3075, 4.53291, 4.54404, 4.55091, 4.54061, 4.81057, 4.56482, 4.63101, 4.49151, 4.63967, 4.5821, 4.63176, 4.53436, 4.4525, 4.48126, 4.56776, 4.72961, 4.60447, 4.49692, 4.5227, 4.50968, 4.44675, 4.49839, 4.46134, 4.71005, 4.54404, 4.42861, 4.39031, 4.79081, 4.41785, 4.43083, 4.35271, 4.52753, 4.52785, 4.22895, 4.47809, 4.68169, 4.66466, 4.65804, 4.39191, 4.4413, 4.38979, 4.53647, 4.37195, 4.62103, 4.58251, 4.53131, 4.64613, 5.05604, 5.03449, 4.84351, 4.92357, 5.02884, 4.92837, 5.01349, 5.12242, 4.75762, 4.97021, 5.05851, 4.75947, 4.98536, 4.53884, 4.75816, 4.74583, 5.15535, 4.72651, 5.0038, 4.72036, 4.6808, 5.01636, 5.03725, 4.6792, 4.59079, 4.5991, 4.77306, 4.82085, 4.74839, 4.59973, 4.67423, 4.97407, 4.94202, 4.82236, 4.80984, 4.71256, 4.55784, 4.55088, 4.92069, 5.1637, 4.95192, 4.7477, 4.81613, 4.68816, 4.78189, 4.7817, 4.4923, 4.71061, 4.70764, 4.78757, 4.71949, 4.7465, 4.47507, 4.72662, 4.71206, 5.12464, 4.62008, 4.60929, 4.41944, 4.58794, 4.44068, 4.59014, 4.41696, 4.80983, 4.79266, 4.59093, 4.51193, 4.66466, 4.58033, 4.6739, 4.51589, 4.58396, 4.5999, 4.77647, 4.5057, 4.49631, 4.43182, 4.5949, 4.62978, 4.48854, 4.58804, 4.55901, 4.83874, 4.61534, 4.42463, 4.67042, 4.51236, 4.86842, 4.83339, 4.61706, 4.47709, 4.70206, 4.75398, 4.69523, 4.8414, 4.59893, 4.6948, 4.80736, 4.73687, 4.69443, 4.34524, 4.63093, 4.60673, 4.8731, 4.61145, 4.42092, 4.70009, 4.65739, 4.44436, 4.59815, 4.78113, 4.79099, 4.65715, 4.76346, 4.54009, 5.4109, 5.09409, 5.43987, 5.18111, 5.18355, 5.26623, 5.21926, 5.06959, 5.09965, 5.10376, 5.13237, 4.66241, 5.19213, 5.13166, 5.21161, 4.74348, 5.03923, 5.35143, 4.36153, 4.85343, 4.53917, 4.62071, 4.59175, 4.61896, 4.7143, 4.52582, 4.46192, 4.62817, 4.68721, 4.76058, 4.79086, 4.58841, 4.66999, 4.45808, 4.73794, 4.49805, 4.82108, 4.6904, 4.63219, 4.63669, 4.32457, 4.6131, 4.38634, 4.9146, 4.19484, 4.40309, 4.38799, 4.21587, 4.39033, 4.50687, 4.21381, 4.15566, 4.44562, 4.77204, 4.58408, 5.27321, 4.40803, 5.02492, 4.62078, 4.9517, 5.09257, 4.56707, 4.82894, 4.67496, 4.70067, 5.13655, 4.96508, 4.76591, 4.90553, 5.02625, 4.4807, 5.09348, 4.56321, 4.82452, 4.57235, 4.82558, 4.78788, 5.035, 4.63361, 4.99217, 4.50432, 4.73674, 4.93731, 4.67667, 4.86205, 4.61951, 4.68238, 5.01204, 4.77613, 4.97465, 4.93948, 4.78033, 4.79644, 4.50217, 4.34554, 4.32318, 4.39936, 4.29937, 4.63648, 4.54348, 4.46101, 4.29272, 4.6509, 4.12232, 4.22417, 4.70624, 4.30735, 4.5982, 4.27666, 4.18547, 4.60064, 4.44373, 4.21357, 4.40816, 4.23427, 4.59694, 4.45034, 4.48253, 4.84104, 4.95149, 4.43622, 4.71049, 4.56469, 4.72608, 4.74778, 4.39242, 4.71671, 4.57723, 4.56472, 4.58316, 4.48682, 4.67821, 4.71622, 4.61122, 4.72741, 4.46474, 4.38435, 4.60785, 4.51439, 4.27303, 4.36531, 4.66132, 4.28768, 4.30674, 4.61424, 4.35411, 4.76166, 4.49662, 4.416, 4.41445, 4.40238, 4.50491, 4.21418, 4.43993, 4.50968, 4.85925, 4.81411, 4.75061, 4.94357, 4.71268, 4.87357, 4.93203, 4.76095, 5.15719, 5.38356, 5.04667, 5.17806, 5.27898, 5.28206, 5.02448, 5.18408, 5.28215, 5.04015, 5.33966, 5.07295, 5.18582]
calc = []
calc2 = []
col = []
y1 = [4.11908, 4.56098, 4.66002, 4.40617, 4.43884, 4.33798, 4.39121, 4.34075, 4.28977, 4.50703, 4.33675, 4.52865, 4.23395, 4.40224, 4.3546, 4.37765, 4.64952, 4.5414, 4.38449, 4.46543, 4.3075, 4.53291, 4.54404, 4.55091, 4.54061, 4.81057, 4.56482, 4.63101, 4.49151, 4.63967, 4.5821, 4.63176, 4.53436, 4.4525, 4.48126, 4.56776, 4.72961, 4.60447, 4.49692, 4.5227, 4.50968, 4.44675, 4.49839, 4.46134, 4.71005, 4.54404, 4.42861, 4.39031, 4.79081, 4.41785, 4.43083, 4.35271, 4.52753, 4.52785, 4.22895, 4.47809, 4.68169, 4.66466, 4.65804, 4.39191, 4.4413, 4.38979, 4.53647, 4.37195, 4.62103, 4.58251, 4.53131, 4.64613, 5.05604, 5.03449, 4.84351, 4.92357, 5.02884, 4.92837, 5.01349, 5.12242, 4.75762, 4.97021, 5.05851, 4.75947, 4.98536, 4.53884, 4.75816, 4.74583, 5.15535, 4.72651, 5.0038, 4.72036, 4.6808, 5.01636, 5.03725, 4.6792, 4.59079, 4.5991, 4.77306, 4.82085, 4.74839, 4.59973, 4.67423, 4.97407, 4.94202, 4.82236, 4.80984, 4.71256, 4.55784, 4.55088, 4.92069, 5.1637, 4.95192, 4.7477, 4.81613, 4.68816, 4.78189, 4.7817, 4.4923, 4.71061, 4.70764, 4.78757, 4.71949, 4.7465, 4.47507, 4.72662, 4.71206, 5.12464, 4.62008, 4.60929, 4.41944, 4.58794, 4.44068, 4.59014, 4.41696, 4.80983, 4.79266, 4.59093, 4.51193, 4.66466, 4.58033, 4.6739, 4.51589, 4.58396, 4.5999, 4.77647, 4.5057, 4.49631, 4.43182, 4.5949, 4.62978, 4.48854, 4.58804, 4.55901, 4.83874, 4.61534, 4.42463, 4.67042, 4.51236, 4.86842, 4.83339, 4.61706, 4.47709, 4.70206, 4.75398, 4.69523, 4.8414, 4.59893, 4.6948, 4.80736, 4.73687, 4.69443, 4.34524, 4.63093, 4.60673, 4.8731, 4.61145, 4.42092, 4.70009, 4.65739, 4.44436, 4.59815, 4.78113, 4.79099, 4.65715, 4.76346, 4.54009, 5.4109, 5.09409, 5.43987, 5.18111, 5.18355, 5.26623, 5.21926, 5.06959, 5.09965, 5.10376, 5.13237, 4.66241, 5.19213, 5.13166, 5.21161, 4.74348, 5.03923, 5.35143, 4.36153, 4.85343, 4.53917, 4.62071, 4.59175, 4.61896, 4.7143, 4.52582, 4.46192, 4.62817, 4.68721, 4.76058, 4.79086, 4.58841, 4.66999, 4.45808, 4.73794, 4.49805, 4.82108, 4.6904, 4.63219, 4.63669, 4.32457, 4.6131, 4.38634, 4.9146, 4.19484, 4.40309, 4.38799, 4.21587, 4.39033, 4.50687, 4.21381, 4.15566, 4.44562, 4.77204, 4.58408, 5.27321, 4.40803, 5.02492, 4.62078, 4.9517, 5.09257, 4.56707, 4.82894, 4.67496, 4.70067, 5.13655, 4.96508, 4.76591, 4.90553, 5.02625, 4.4807, 5.09348, 4.56321, 4.82452, 4.57235, 4.82558, 4.78788, 5.035, 4.63361, 4.99217, 4.50432, 4.73674, 4.93731, 4.67667, 4.86205, 4.61951, 4.68238, 5.01204, 4.77613, 4.97465, 4.93948, 4.78033, 4.79644, 4.50217, 4.34554, 4.32318, 4.39936, 4.29937, 4.63648, 4.54348, 4.46101, 4.29272, 4.6509, 4.12232, 4.22417, 4.70624, 4.30735, 4.5982, 4.27666, 4.18547, 4.60064, 4.44373, 4.21357, 4.40816, 4.23427, 4.59694, 4.45034, 4.48253, 4.84104, 4.95149, 4.43622, 4.71049, 4.56469, 4.72608, 4.74778, 4.39242, 4.71671, 4.57723, 4.56472, 4.58316, 4.48682, 4.67821, 4.71622, 4.61122, 4.72741, 4.46474, 4.38435, 4.60785, 4.51439, 4.27303, 4.36531, 4.66132, 4.28768, 4.30674, 4.61424, 4.35411, 4.76166, 4.49662, 4.416, 4.41445, 4.40238, 4.50491, 4.21418, 4.43993, 4.50968, 4.85925, 4.81411, 4.75061, 4.94357, 4.71268, 4.87357, 4.93203, 4.76095, 5.15719, 5.38356, 5.04667, 5.17806, 5.27898, 5.28206, 5.02448, 5.18408, 5.28215, 5.04015, 5.33966, 5.07295, 5.18582]
y2 = [3.75, 3.82, 3.9, 3.87, 4.06, 3.77, 4.01, 3.92, 3.87, 3.93, 3.83, 3.77, 4.03, 3.81, 3.76, 3.95, 3.73, 4, 3.88, 3.95, 3.85, 3.84, 3.91, 3.84, 4, 4.05, 4.02, 3.97, 4.03, 4.03, 3.95, 4.07, 3.98, 4.12, 3.96, 3.98, 4, 3.86, 4.04, 3.92, 4, 3.92, 4.01, 3.95, 3.91, 3.97, 4.06, 3.97, 4.08, 4.02, 4.03, 4.06, 4, 4, 3.94, 4.09, 4.11, 3.97, 3.99, 4.02, 3.9, 3.91, 4.02, 3.96, 3.97, 3.96, 3.95, 4.63, 4.86, 4.64, 4.87, 4.73, 4.82, 4.66, 4.71, 4.79, 4.83, 4.73, 4.72, 4.77, 4.79, 4.63, 4.76, 4.67, 4.57, 4.61, 4.7, 4.71, 4.56, 4.57, 4.64, 4.34, 4.4, 4.45, 4.51, 4.55, 4.4, 4.55, 4.49, 4.54, 4.61, 4.42, 4.36, 4.26, 4.4, 4.31, 4.53, 4.54, 4.32, 4.39, 4.36, 4.5, 4.53, 4.48, 4.31, 4.49, 4.46, 4.42, 4.49, 4.47, 4.35, 4.63, 4.57, 5.84, 4.38, 4.14, 4.15, 4.18, 4.24, 4.22, 4.12, 4.09, 4.27, 4.19, 4.04, 4.07, 4.24, 4.21, 4.12, 4.3, 4, 4.25, 4.24, 4.32, 4.23, 4.22, 4.18, 4.18, 4.25, 4.04, 4.31, 4.16, 4.1, 4.24, 4.28, 4.18, 4.25, 4.33, 4.09, 4.31, 4.07, 4.26, 4.18, 4.23, 4.18, 4.21, 4.14, 4.19, 4.18, 4.24, 4.27, 4.23, 4.24, 4.03, 4.25, 4.32, 4.09, 4.27, 4.18, 4.24, 4.35, 4.17, 4.13, 5.18, 4.8, 5.53, 4.95, 4.91, 4.77, 4.94, 5.35, 4.98, 5.08, 4.82, 4.75, 4.88, 4.95, 5.08, 4.71, 4.87, 5.99, 4.13, 4.19, 4.08, 4.23, 4.15, 4.36, 4.05, 4.11, 4.07, 4.05, 4.21, 4.19, 4.21, 4.08, 4.03, 4.06, 4.11, 4.02, 4.09, 4.15, 4.1, 4.1, 4.07, 4.02, 4, 4.22, 3.47, 3.66, 3.56, 3.57, 3.54, 3.61, 3.55, 3.67, 3.52, 4.3, 4.33, 4.5, 4.35, 4.45, 4.35, 4.37, 4.51, 4.51, 4.39, 4.42, 4.29, 4.25, 4.61, 4.38, 4.54, 4.31, 4.32, 4.52, 4.37, 4.53, 4.31, 4.45, 4.47, 4.47, 4.27, 4.36, 4.32, 4.31, 4.33, 4.35, 4.66, 4.34, 4.4, 4.42, 4.3, 4.45, 4.46, 4.37, 4.43, 3.43, 3.6, 3.45, 3.59, 3.51, 3.63, 3.48, 3.56, 3.62, 3.52, 3.45, 3.53, 3.73, 3.1, 3.46, 3.37, 3.42, 3.62, 3.65, 3.47, 3.72, 3.47, 3.7, 3.67, 3.47, 4.07, 3.93, 3.86, 3.95, 3.96, 3.77, 3.96, 3.9, 3.76, 3.94, 3.9, 3.89, 3.9, 3.96, 3.92, 3.82, 3.83, 3.72, 3.85, 3.74, 3.75, 3.72, 3.61, 3.74, 3.84, 3.8, 3.89, 3.7, 3.83, 3.84, 3.89, 3.86, 3.79, 3.93, 3.82, 3.77, 3.77, 3.83, 4.18, 4.06, 4.19, 4.09, 4.13, 4.2, 4.06, 4.72, 4.8, 4.51, 4.65, 4.96, 4.91, 4.76, 5.25, 4.76, 4.68, 4.96, 4.68, 4.62]
y3 = [0.82625, 0.921676, 1.0379, 1.0531, 0.7964, 0.7571, 1.0715, 1.10726, 0.883331, 1.0051, 0.914411, 0.914971, 0.991509, 0.9939, 0.941024, 1.0275, 0.898842, 1.04, 1.0456, 1.0475, 1.0075, 1.1944, 1.0019, 1.1944, 1.18, 1.07153, 1.2396, 1.27149, 1.3091, 1.2091, 1.21147, 1.0851, 1.1012, 0.975344, 1.1384, 1.0996, 1.18, 1.2004, 1.0584, 1.14726, 1.12, 0.959936, 1.1291, 1.15148, 1.21478, 1.14671, 0.9364, 1.05149, 1.26006, 0.9996, 0.986691, 0.9964, 1.14, 1.02, 1.18116, 1.1419, 1.1979, 1.2491, 1.1307, 1.2196, 1.0658, 1.2219, 1.1796, 1.2384, 1.26671, 1.1384, 1.30352, 1.11873, 1.5804, 1.2304, 1.0131, 1.31337, 1.1276, 1.04156, 1.40406, 1.39646, 1.0811, 1.2771, 1.1616, 1.02957, 1.3859, 1.2931, 1.20898, 1.25919, 1.63625, 1.1579, 1.31, 1.2659, 1.31846, 1.5651, 1.4704, 1.05604, 1.04, 1.1675, 0.986499, 0.9875, 1.1736, 0.994525, 1.1699, 1.1084, 1.1979, 1.06824, 1.2003, 1.08945, 0.9464, 1.10814, 1.2491, 1.14228, 0.970976, 1.0379, 0.8904, 0.8675, 1.09431, 1.2103, 0.988139, 1.1299, 0.9684, 1.0636, 1.0883, 1.06891, 1.03828, 1.14747, 1.1651, 3.78186, 1.1956, 1.049, 0.995275, 1.2276, 1.0224, 0.9316, 1.05586, 1.07462, 1.2971, 1.0939, 1.07518, 0.8251, 1.26218, 1.2059, 1.00611, 1.0451, 1.04, 1.3075, 0.9824, 0.784224, 0.918171, 0.9516, 1.1076, 0.942324, 0.9875, 1.11518, 1.2339, 1.0344, 1.0219, 1.26262, 1.01842, 1.0676, 1.06688, 1.0011, 1.2219, 1.01966, 0.979451, 1.2724, 1.20232, 1.1171, 1.2876, 0.9659, 1.169, 1.0939, 1.04232, 1.20262, 1.2571, 1.17817, 0.9824, 1.20669, 1.30812, 1.11098, 1.19462, 1.35943, 1.3476, 1.30218, 1.0675, 1.2611, 1.1131, 1.49928, 1.18, 1.25491, 1.5275, 1.2419, 1.5371, 1.42044, 1.12128, 0.7996, 1.17554, 1.25528, 1.18188, 1.3056, 1.35252, 1.4536, 1.5459, 1.49027, 1.4299, 1.40367, 1.3939, 1.3736, 1.3971, 1.5475, 1.5803, 1.36347, 1.2379, 1.2051, 1.16347, 1.30314, 1.4139, 1.4059, 1.2936, 1.3691, 1.2964, 1.1979, 1.458, 1.3419, 1.41528, 1.41, 1.41, 1.3251, 1.4596, 1.26, 1.4516, 0.809509, 0.8044, 0.892928, 0.877651, 0.943084, 0.987579, 0.881475, 1.06641, 1.0096, 1.2602, 1.3411, 1.7325, 1.4875, 1.3675, 1.2875, 1.7931, 1.4699, 1.2699, 1.2579, 1.47896, 1.2859, 1.72687, 1.66538, 1.60744, 1.2084, 1.3939, 1.2976, 1.6696, 1.3131, 1.4091, 1.20814, 1.24947, 1.6491, 1.34929, 1.23477, 1.4005, 1.51098, 1.2739, 1.4211, 1.45672, 1.64156, 1.4644, 1.46, 1.3836, 1.6949, 1.5275, 1.36732, 1.6131, 1.3851, 1.56745, 1.4296, 1.0675, 1.0419, 1.1531, 1.64487, 1.4885, 1.3264, 1.2956, 1.4535, 1.30848, 1.3291, 1.37623, 1.3739, 1.3684, 1.10667, 1.36056, 1.3956, 1.28072, 1.14869, 1.41837, 1.06869, 1.5269, 1.3211, 1.22869, 1.5051, 1.4051, 1.1604, 1.45955, 1.2784, 1.65497, 1.44158, 1.45, 1.3224, 1.33164, 1.2858, 1.28922, 1.29, 1.50158, 1.4936, 1.28168, 1.25441, 1.33998, 0.999275, 1.3324, 1.2475, 1.25998, 1.08758, 1.25228, 1.14186, 1.08, 1.32054, 1.33, 1.26779, 1.2144, 1.1779, 1.2494, 1.2659, 1.39955, 1.2876, 1.17923, 1.17923, 1.94779, 1.9676, 1.5764, 1.9739, 1.8819, 1.66367, 1.8236, 1.85156, 1.8616, 2.6096, 2.0299, 1.9475, 1.78442, 1.9619, 1.7824, 1.95188, 2.28898, 2.41662, 2.4784, 1.89662, 1.9956]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
#c2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

avg = 0

for i in range(0, len(y1)):
	if y1[i] <= 4.5:
		y1[i] = 1
	elif y1[i] <= 5:
		y1[i] = 1
	else:
		y1[i] = 1
	if y3[i] <= 3:
		calc.append(-1.73 + 1.66 * ((y2[i] ** 0.5) * 1.5 + (y3[i] ** 0.5) * 0.7))
		calc2.append(diffi[i])
		col.append(y1[i])
		avg = avg - 1.73 + 1.66 * ((y2[i] ** 0.5) * 1.5 + (y3[i] ** 0.5) * 0.7);

avg = avg / len(calc)

coeff = polyfit(calc2, calc, 1)
coeff = [1, 0]

vl2 = 0
vl = 0

for i in range(0, len(calc)):
	vl = vl + (calc[i] - avg) ** 2
	vl2 = vl2 + (calc[i] - (calc2[i] * coeff[0] + coeff[1])) ** 2

print((vl - vl2) / vl)

cmap = mpl.colormaps.get_cmap("gist_rainbow")

plt.xticks(fontproperties = 'Times New Roman', fontsize = 8)
plt.yticks(fontproperties = 'Times New Roman', fontsize = 8)
# plt.title("Cluster Difficulty Analysis", fontdict = {'family' : 'Times New Roman', 'size':15})
# plt.xlabel("average of percentages", fontdict = {'family' : 'Times New Roman', 'size':10})
# plt.ylabel("variance of percentages", fontdict = {'family' : 'Times New Roman', 'size':10})
plt.scatter(calc2, calc, c="b", cmap=cmap)
x = np.linspace(3.75, 5.75, 100)
plt.plot(x, coeff[0] * x + coeff[1], c="r")
plt.savefig('./Test.png', dpi = 300, bbox_inches = "tight")
plt.show()