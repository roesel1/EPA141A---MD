from ema_workbench import Scenario

# def create_scenario(
#     var_list
    # discount_rate_0,
    # discount_rate_1,
    # discount_rate_2,
    # A_0_ID_flood_wave_shape,
    # A_1_Bmax,
    # A_1_pfail,
    # A_1_Brate,
    # A_2_Bmax,
    # A_2_pfail,
    # A_2_Brate,
    # A_3_Bmax,
    # A_3_pfail,
    # A_3_Brate,
    # A_4_Bmax,
    # A_4_pfail,
    # A_4_Brate,
    # A_5_Bmax,
    # A_5_pfail,
    # A_5_Brate
# ):
#
#     return Scenario("SCEN1", **{
#         'discount rate 0': discount_rate_0,
#         'discount rate 1': discount_rate_1,
#         'discount rate 2': discount_rate_2,
#         'A.0_ID flood wave shape': A_0_ID_flood_wave_shape,
#         'A.1_Bmax': A_1_Bmax,
#         'A.1_pfail': A_1_pfail,
#         'A.1_Brate': A_1_Brate,
#         'A.2_Bmax': A_2_Bmax,
#         'A.2_pfail': A_2_pfail,
#         'A.2_Brate': A_2_Brate,
#         'A.3_Bmax': A_3_Bmax,
#         'A.3_pfail': A_3_pfail,
#         'A.3_Brate': A_3_Brate,
#         'A.4_Bmax': A_4_Bmax,
#         'A.4_pfail': A_4_pfail,
#         'A.4_Brate': A_4_Brate,
#         'A.5_Bmax': A_5_Bmax,
#         'A.5_pfail': A_5_pfail,
#         'A.5_Brate': A_5_Brate
#     })


def create_scenario(
    var_list
):

    return Scenario("SCEN1", **{
        'discount rate 0': var_list[0],
        'discount rate 1': var_list[1],
        'discount rate 2': var_list[2],
        'A.0_ID flood wave shape': var_list[3],
        'A.1_Bmax': var_list[4],
        'A.1_pfail': var_list[5],
        'A.1_Brate': var_list[6],
        'A.2_Bmax': var_list[7],
        'A.2_pfail': var_list[8],
        'A.2_Brate': var_list[9],
        'A.3_Bmax': var_list[10],
        'A.3_pfail': var_list[11],
        'A.3_Brate': var_list[12],
        'A.4_Bmax': var_list[13],
        'A.4_pfail': var_list[14],
        'A.4_Brate': var_list[15],
        'A.5_Bmax': var_list[16],
        'A.5_pfail': var_list[17],
        'A.5_Brate': var_list[18]
    })


# para_list = []
# for uncertainty in dike_model.uncertainties:
#     # print((variable in df_param_space_A5.Variable))
#     variable = uncertainty.name
#     print(variable)
#     if (variable in list(df_param_space_A5.Variable)) & (variable in list(df_param_space_all.Variable)):
#
#         min_1 = float(df_param_space_A5[df_param_space_A5['Variable'] == variable][df_param_space_A5.columns[1]].values[
#                           0]) * 10000
#         max_1 = float(df_param_space_A5[df_param_space_A5['Variable'] == variable][df_param_space_A5.columns[2]].values[
#                           0]) * 10000
#
#         min_2 = float(
#             df_param_space_all[df_param_space_all['Variable'] == variable][df_param_space_all.columns[1]].values[
#                 0]) * 10000
#         max_2 = float(
#             df_param_space_all[df_param_space_all['Variable'] == variable][df_param_space_all.columns[2]].values[
#                 0]) * 10000
#         print(variable)
#         boundaries = mr.overlap(range(int(min_1), int(max_1)), range(int(min_2), int(max_2)))
#         para_list.append((boundaries.start + (boundaries.stop - boundaries.start) / 2) / 10000)
#     elif (variable in list(df_param_space_A5.Variable)):
#         min_1 = float(
#             df_param_space_A5[df_param_space_A5['Variable'] == variable][df_param_space_A5.columns[1]].values[0])
#         max_1 = float(
#             df_param_space_A5[df_param_space_A5['Variable'] == variable][df_param_space_A5.columns[2]].values[0])
#         para_list.append((min_1 + (max_1 - min_1) / 2))
#
#     elif (variable in list(df_param_space_all.Variable)):
#         min_2 = float(
#             df_param_space_all[df_param_space_all['Variable'] == variable][df_param_space_all.columns[1]].values[0])
#         max_2 = float(
#             df_param_space_all[df_param_space_all['Variable'] == variable][df_param_space_all.columns[2]].values[0])
#         para_list.append((min_2 + (max_2 - min_2) / 2))
#     elif variable.startswith("d"):
#         para_list.append(3.5)
#     elif variable == "A.0_ID flood wave shape":
#         para_list.append(17)
#     elif variable.endswith("Brate"):
#         para_list.append(1.5)
#     else:
#         para_list.append((uncertainty.lower_bound + (uncertainty.upper_bound - uncertainty.lower_bound) / 2))
#
# PRIM_overlap_scenario = create_scenario(para_list)

