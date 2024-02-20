from pathlib import Path


pilot_experiment = ['A102_amu_v_3', 'A102_ang_p_3', 'A102_ang_v_2', 'A102_anx_p_2', 'A102_anx_p_3', 'A102_bor_p_2', 'A102_bor_p_3', 'A102_conc_p_3', 'A102_conc_v_2', 'A102_conf_p_3', 'A102_conf_v_2', 'A102_det_v_3', 'A102_disa_v_2', 'A102_disa_v_3', 'A102_disg_p_3', 'A102_disg_v_3', 'A102_dist_p_3', 'A102_emb_p_2', 'A102_emb_v_3', 'A102_env_p_3', 'A102_exc_p_3', 'A102_exc_v_3', 'A102_fea_p_2', 'A102_fea_p_3', 'A102_gra_p_3', 'A102_gra_v_3', 'A102_mov_v_3', 'A102_neg_sur_p_2', 'A102_neg_sur_p_3', 'A102_neu_sit1_v', 'A102_neu_sit2_v', 'A102_nos_p_2', 'A102_nos_p_3', 'A102_pea_p_2', 'A102_ple_p_2', 'A102_ple_v_2', 'A102_pos_sur_p_3', 'A102_rel_p_2', 'A102_rel_p_3', 'A102_sad_p_2', 'A102_sad_p_3', 'A102_sar_p_2', 'A102_sat_p_3', 'A102_scha_p_3', 'A102_scha_v_2', 'A102_sex_p_2', 'A102_sex_p_3', 'A102_ten_v_3', 'A102_tri_p_2', 'A102_tri_p_3', 'A200_amu_v_2', 'A200_det_p_3', 'A200_dist_p_2', 'A200_int_v_2', 'A200_int_v_3', 'A200_pos_sur_p_3', 'A200_sar_p_2', 'A205_cont_p_2', 'A205_cont_p_3', 'A205_hap_p_3', 'A205_hap_v_3', 'A205_mov_p_3', 'A205_rej_v_2', 'A205_rej_v_3', 'A205_sat_v_3', 'A205_ten_p_3', 'A207_dou_v_2', 'A207_dou_v_3', 'A207_pea_v_2', 'A220_adm_v_3', 'A220_hop_p_2', 'A220_ins_v_2', 'A220_pri_p_3', 'A221_awe_p_2', 'A221_sha_p_2', 'A221_sha_v_2', 'A227_adm_p_3', 'A227_gui_v_3', 'A227_hop_p_3', 'A227_pri_p_2', 'A227_reg_v_3', 'A303_env_p_3', 'A323_awe_v_2', 'A327_ele_p_3', 'A334_reg_p_2', 'A407_ins_p_2', 'A424_ele_v_3', 'A55_gui_v_2_ver1']
# pilot_intro = ['A67_pea_v_3', 'A72_det_p_3', 'A91_ang_p_3']

all_filenames = set(pilot_experiment)

print(all_filenames)
print(len(all_filenames))


def belongs_to_appraisal_pilot(filename):
    filename_no_ext = Path(filename).stem

    if filename_no_ext in all_filenames:
        return True
    else:
        return False
