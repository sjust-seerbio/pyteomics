_protxml_schema_defaults = {'bools': set(),
 'charlists': set(),
 'floatlists': set(),
 'floats': {('ASAPRatio', 'heavy2light_ratio_mean'),
  ('ASAPRatio', 'heavy2light_ratio_standard_dev'),
  ('ASAPRatio', 'ratio_mean'),
  ('ASAPRatio', 'ratio_standard_dev'),
  ('ASAPRatio_pvalue', 'adj_ratio_mean'),
  ('ASAPRatio_pvalue', 'adj_ratio_standard_dev'),
  ('ASAPRatio_pvalue', 'decimal_pvalue'),
  ('ASAPRatio_pvalue', 'heavy2light_adj_ratio_mean'),
  ('ASAPRatio_pvalue', 'heavy2light_adj_ratio_standard_dev'),
  ('ASAPRatio_pvalue', 'pvalue'),
  ('ASAP_Peak', 'heavy2light_ratio_mean'),
  ('ASAP_Peak', 'heavy2light_ratio_standard_dev'),
  ('ASAP_Peak', 'ratio_mean'),
  ('ASAP_Peak', 'ratio_standard_dev'),
  ('ASAP_Peak', 'weight'),
  ('ASAP_Seq', 'heavy2light_ratio_mean'),
  ('ASAP_Seq', 'heavy2light_ratio_standard_dev'),
  ('ASAP_Seq', 'ratio_mean'),
  ('ASAP_Seq', 'ratio_standard_dev'),
  ('ASAP_Seq', 'weight'),
  ('ASAP_prot_analysis_summary', 'min_peptide_probability'),
  ('ASAP_prot_analysis_summary', 'min_peptide_weight'),
  ('ASAP_prot_analysis_summary', 'min_protein_probability'),
  ('ASAP_pvalue_analysis_summary', 'background_fitting_error'),
  ('ASAP_pvalue_analysis_summary', 'background_ratio_mean'),
  ('ASAP_pvalue_analysis_summary', 'background_ratio_stdev'),
  ('StPeterQuant', 'SIn'),
  ('StPeterQuant', 'ng'),
  ('StPeterQuant_peptide', 'spectralIndex'),
  ('StPeter_analysis_summary', 'FDR'),
  ('StPeter_analysis_summary', 'probability'),
  ('StPeter_analysis_summary', 'sampleLoad'),
  ('StPeter_analysis_summary', 'tolerance'),
  ('XPress_analysis_summary', 'min_peptide_probability'),
  ('XPress_analysis_summary', 'min_peptide_weight'),
  ('XPress_analysis_summary', 'min_protein_probability'),
  ('affected_channel', 'correction'),
  ('decoy_analysis_summary', 'decoy_ratio'),
  ('error_point', 'error'),
  ('error_point', 'min_prob'),
  ('fpkm_distribution', 'alt_pos_to_neg_ratio'),
  ('fpkm_distribution', 'fpkm_lower_bound_excl'),
  ('fpkm_distribution', 'fpkm_lower_bound_incl'),
  ('fpkm_distribution', 'neg_freq'),
  ('fpkm_distribution', 'pos_freq'),
  ('fpkm_distribution', 'pos_to_neg_ratio'),
  ('fragment_masses', 'mz'),
  ('indistinguishable_peptide', 'calc_neutral_pep_mass'),
  ('intensity', 'error'),
  ('intensity', 'mz'),
  ('intensity', 'ratio'),
  ('libra_summary', 'mass_tolerance'),
  ('libra_summary', 'min_pep_prob'),
  ('libra_summary', 'min_pep_wt'),
  ('libra_summary', 'min_prot_prob'),
  ('ni_distribution', 'alt_pos_to_neg_ratio'),
  ('ni_distribution', 'neg_freq'),
  ('ni_distribution', 'ni_lower_bound_excl'),
  ('ni_distribution', 'ni_lower_bound_incl'),
  ('ni_distribution', 'pos_freq'),
  ('ni_distribution', 'pos_to_neg_ratio'),
  ('nsp_distribution', 'alt_pos_to_neg_ratio'),
  ('nsp_distribution', 'neg_freq'),
  ('nsp_distribution', 'nsp_lower_bound_excl'),
  ('nsp_distribution', 'nsp_lower_bound_incl'),
  ('nsp_distribution', 'pos_freq'),
  ('nsp_distribution', 'pos_to_neg_ratio'),
  ('peptide', 'calc_neutral_pep_mass'),
  ('peptide', 'exp_sibling_ion_bin'),
  ('peptide', 'exp_sibling_ion_instances'),
  ('peptide', 'exp_tot_instances'),
  ('peptide', 'fpkm_adjusted_probability'),
  ('peptide', 'initial_probability'),
  ('peptide', 'max_fpkm'),
  ('peptide', 'n_sibling_peptides'),
  ('peptide', 'ni_adjusted_probability'),
  ('peptide', 'nsp_adjusted_probability'),
  ('peptide', 'weight'),
  ('point', 'fdr_pp'),
  ('point', 'fdr_pp_decoy'),
  ('point', 'logratio'),
  ('point', 'model_distr'),
  ('point', 'num_corr_pp'),
  ('point', 'num_corr_pp_decoy'),
  ('point', 'obs_distr'),
  ('point', 'pp_decoy_uncert'),
  ('point', 'pp_uncert'),
  ('point', 'prob_cutoff'),
  ('protein', 'confidence'),
  ('protein', 'percent_coverage'),
  ('protein', 'probability'),
  ('protein_group', 'probability'),
  ('protein_summary_data_filter', 'false_positive_error_rate'),
  ('protein_summary_data_filter', 'min_probability'),
  ('protein_summary_data_filter', 'predicted_num_correct'),
  ('protein_summary_data_filter', 'predicted_num_incorrect'),
  ('protein_summary_data_filter', 'sensitivity'),
  ('protein_summary_header', 'initial_min_peptide_prob'),
  ('protein_summary_header', 'min_peptide_probability'),
  ('protein_summary_header', 'min_peptide_weight'),
  ('protein_summary_header', 'num_predicted_correct_prots'),
  ('protein_summary_header', 'total_no_spectrum_ids')},
 'intlists': set(),
 'ints': {('ASAPRatio', 'ratio_number_peptides'),
  ('ASAP_Peak', 'datanum'),
  ('ASAP_Seq', 'datanum'),
  ('ASAP_pvalue_analysis_summary', 'asap_prot_id'),
  ('ASAP_pvalue_analysis_summary', 'asapratio_id'),
  ('StPeterQuant_peptide', 'charge'),
  ('affected_channel', 'channel'),
  ('analysis_result', 'id'),
  ('analysis_summary', 'id'),
  ('contributing_channel', 'channel'),
  ('error_point', 'num_corr'),
  ('error_point', 'num_incorr'),
  ('fpkm_distribution', 'bin_no'),
  ('fragment_masses', 'channel'),
  ('intensity', 'channel'),
  ('libra_result', 'number'),
  ('libra_summary', 'centroiding_preference'),
  ('libra_summary', 'normalization'),
  ('libra_summary', 'output_type'),
  ('ni_distribution', 'bin_no'),
  ('nsp_distribution', 'bin_no'),
  ('peptide', 'charge'),
  ('peptide', 'fpkm_bin'),
  ('peptide', 'n_enzymatic_termini'),
  ('peptide', 'n_instances'),
  ('peptide', 'n_sibling_peptides_bin'),
  ('protein', 'n_indistinguishable_proteins'),
  ('protein', 'total_number_distinct_peptides'),
  ('protein', 'total_number_peptides'),
  ('protein_summary_header', 'num_input_1_spectra'),
  ('protein_summary_header', 'num_input_2_spectra'),
  ('protein_summary_header', 'num_input_3_spectra'),
  ('protein_summary_header', 'num_input_4_spectra'),
  ('protein_summary_header', 'num_input_5_spectra')},
 'lists': {'ASAP_Dta',
  'ASAP_Peak',
  'ASAP_Seq',
  'StPeterQuant_peptide',
  'affected_channel',
  'analysis_result',
  'analysis_summary',
  'contributing_channel',
  'error_point',
  'fpkm_distribution',
  'fpkm_information',
  'fragment_masses',
  'indistinguishable_peptide',
  'indistinguishable_protein',
  'intensity',
  'mod_aminoacid_mass',
  'modification_info',
  'ni_distribution',
  'ni_information',
  'nsp_distribution',
  'parameter',
  'peptide',
  'peptide_parent_protein',
  'point',
  'protein',
  'protein_group',
  'protein_summary_data_filter'}}

_mzid_schema_defaults = {'bools': {('Enzyme', 'semiSpecific'),
      ('Enzymes', 'independent'),
      ('PeptideEvidence', 'isDecoy'),
      ('ProteinDetectionHypothesis', 'passThreshold'),
      ('SearchModification', 'fixedMod'),
      ('SpectrumIdentificationItem', 'passThreshold')},
 'charlists': {('Modification', 'residues'),
      ('SearchModification', 'residues')},
 'floatlists': {('FragmentArray', 'values')},
 'floats': {('Modification', 'avgMassDelta'),
      ('Modification', 'monoisotopicMassDelta'),
      ('Residue', 'mass'),
      ('SearchModification', 'massDelta'),
      ('SpectrumIdentificationItem', 'calculatedMassToCharge'),
      ('SpectrumIdentificationItem', 'calculatedPI'),
      ('SpectrumIdentificationItem', 'experimentalMassToCharge'),
      ('SubstitutionModification', 'avgMassDelta'),
      ('SubstitutionModification', 'monoisotopicMassDelta')},
 'intlists': {('IonType', 'index'), ('MassTable', 'msLevel')},
 'ints': {('BibliographicReference', 'year'),
      ('DBSequence', 'length'),
      ('Enzyme', 'missedCleavages'),
      ('IonType', 'charge'),
      ('Modification', 'location'),
      ('PeptideEvidence', 'end'),
      ('PeptideEvidence', 'start'),
      ('SearchDatabase', 'numDatabaseSequences'),
      ('SearchDatabase', 'numResidues'),
      ('SpectrumIdentificationItem', 'chargeState'),
      ('SpectrumIdentificationItem', 'rank'),
      ('SpectrumIdentificationList', 'numSequencesSearched'),
      ('SubstitutionModification', 'location')},
 'lists': {'Affiliation',
    'AmbiguousResidue',
    'AnalysisSoftware',
    'BibliographicReference',
    'ContactRole',
    'DBSequence',
    'Enzyme',
    'Filter',
    'FragmentArray',
    'InputSpectra',
    'InputSpectrumIdentifications',
    'IonType',
    'MassTable',
    'Measure',
    'Modification',
    'Peptide',
    'PeptideEvidence',
    'PeptideEvidenceRef',
    'PeptideHypothesis',
    'ProteinAmbiguityGroup',
    'ProteinDetectionHypothesis',
    'Residue',
    'Sample',
    'SearchDatabase',
    'SearchDatabaseRef',
    'SearchModification',
    'SourceFile',
    'SpecificityRules',
    'SpectraData',
    'SpectrumIdentification',
    'SpectrumIdentificationItem',
    'SpectrumIdentificationItemRef',
    'SpectrumIdentificationList',
    'SpectrumIdentificationProtocol',
    'SpectrumIdentificationResult',
    'SubSample',
    'SubstitutionModification',
    'TranslationTable',
    'cv',
    'cvParam'}}

_trafoxml_schema_defaults = {'bools': set(),
     'charlists': set(),
     'floatlists': set(),
     'floats': {('Pair', 'from'), ('Pair', 'to'), ('TrafoXML', 'version')},
     'intlists': set(),
     'ints': {('Pairs', 'count')},
     'lists': {'Pair', 'Param'}}

_featurexml_schema_defaults = {'bools': {
    ('PeptideIdentification', 'higher_score_better'),
    ('ProteinIdentification', 'higher_score_better'),
    ('UnassignedPeptideIdentification', 'higher_score_better')},
 'charlists': set(),
 'floatlists': set(),
 'floats': {('PeptideHit', 'score'),
            ('PeptideIdentification', 'MZ'),
            ('PeptideIdentification', 'RT'),
            ('PeptideIdentification', 'significance_threshold'),
            ('ProteinHit', 'score'),
            ('ProteinIdentification', 'significance_threshold'),
            ('SearchParameters', 'peak_mass_tolerance'),
            ('SearchParameters', 'precursor_peak_tolerance'),
            ('UnassignedPeptideIdentification', 'MZ'),
            ('UnassignedPeptideIdentification', 'RT'),
            ('UnassignedPeptideIdentification', 'significance_threshold'),
            ('pt', 'x'), ('pt', 'y'), ('position', 'position'),
            ('feature', 'overallquality'), ('feature', 'intensity')
            },
 'intlists': set(),
 'ints': {('PeptideHit', 'charge'),
          ('PeptideIdentification', 'spectrum_reference'),
          ('SearchParameters', 'missed_cleavages'),
          ('UnassignedPeptideIdentification', 'spectrum_reference'),
          ('featureList', 'count'), ('convexhull', 'nr'),
          ('position', 'dim'), ('feature', 'spectrum_index'),
          ('feature', 'charge'), ('quality', 'dim'), ('quality', 'quality')},
 'lists': {'FixedModification', 'IdentificationRun',
           'PeptideHit', 'PeptideIdentification', 'ProteinHit',
           'UnassignedPeptideIdentification', 'VariableModification',
           'convexhull', 'dataProcessing', 'feature', 'hposition',
           'hullpoint', 'param', 'position', 'processingAction',
           'pt', 'quality', 'userParam'}}

_tandem_schema_defaults = {'ints': {
        ('group', 'z'), ('aa', 'at')} | {('domain', k) for k in [
            'missed_cleavages', 'start', 'end', 'y_ions', 'b_ions',
            'a_ions', 'x_ions', 'c_ions', 'z_ions']},

            'floats': {('group', k) for k in [
                'fI', 'sumI', 'maxI', 'mh', 'expect', 'rt']} | {
                   ('domain', k) for k in [
                       'expect', 'hyperscore', 'b_score', 'y_score',
                       'a_score', 'x_score', 'c_score', 'z_score',
                       'nextscore', 'delta', 'mh']} | {
                   ('protein', 'expect'), ('protein', 'sumI'),
                   ('aa', 'modified')},

            'bools': set(),
            'lists': {'group', 'trace', 'attribute', 'protein', 'aa', 'note'},
            'floatlists': {('values', 'values')},
            'intlists': set(), 'charlists': set()}

_mzxml_schema_defaults = {'bools': {('dataProcessing', 'centroided'),
                                 ('dataProcessing', 'chargeDeconvoluted'),
                                 ('dataProcessing', 'deisotoped'),
                                 ('dataProcessing', 'spotIntegration'),
                                 ('maldi', 'collisionGas'),
                                 ('scan', 'centroided'),
                                 ('scan', 'chargeDeconvoluted'),
                                 ('scan', 'deisotoped')},
                       'charlists': set(),
                       'floatlists': set(),
                       'floats': {('dataProcessing', 'intensityCutoff'),
                                  ('precursorMz', 'precursorIntensity'),
                                  ('precursorMz', 'windowWideness'),
                                  ('precursorMz', 'precursorMz'),
                                  ('scan', 'basePeakIntensity'),
                                  ('scan', 'basePeakMz'),
                                  ('scan', 'cidGasPressure'),
                                  ('scan', 'collisionEnergy'),
                                  ('scan', 'compensationVoltage'),
                                  ('scan', 'endMz'),
                                  ('scan', 'highMz'),
                                  ('scan', 'ionisationEnergy'),
                                  ('scan', 'lowMz'),
                                  ('scan', 'startMz'),
                                  ('scan', 'totIonCurrent')},
                       'duration': {("scan", "retentionTime")
                                    },
                       'intlists': set(),
                       'ints': {('msInstrument', 'msInstrumentID'),
                                ('peaks', 'compressedLen'),
                                ('precursorMz', 'precursorCharge'),
                                ('robot', 'deadVolume'),
                                ('scan', 'msInstrumentID'),
                                ('scan', 'peaksCount'),
                                ('scanOrigin', 'num'),
                                ('scan', 'msLevel')},
                       'lists': {'dataProcessing',
                                 'msInstrument',
                                 'parentFile',
                                 'peaks',
                                 'plate',
                                 'precursorMz',
                                 'scanOrigin',
                                 'spot'}}

_mzml_schema_defaults = {'ints': {
    ('spectrum', 'index'),
     ('instrumentConfigurationList', 'count'),
     ('binaryDataArray', 'encodedLength'),
     ('cvList', 'count'),
     ('binaryDataArray', 'arrayLength'),
     ('scanWindowList', 'count'),
     ('componentList', 'count'),
     ('sourceFileList', 'count'),
     ('productList', 'count'),
     ('referenceableParamGroupList', 'count'),
     ('scanList', 'count'),
     ('spectrum', 'defaultArrayLength'),
     ('dataProcessingList', 'count'),
     ('sourceFileRefList', 'count'),
     ('scanSettingsList', 'count'),
     ('selectedIonList', 'count'),
     ('chromatogram', 'defaultArrayLength'),
     ('precursorList', 'count'),
     ('chromatogram', 'index'),
     ('processingMethod', 'order'),
     ('targetList', 'count'),
     ('sampleList', 'count'),
     ('softwareList', 'count'),
     ('binaryDataArrayList', 'count'),
     ('spectrumList', 'count'),
     ('chromatogramList', 'count')},
        'floats': {},
        'bools': {},
        'lists': {'scan', 'spectrum', 'sample', 'cv', 'dataProcessing',
            'cvParam', 'source', 'userParam', 'detector', 'product',
            'referenceableParamGroupRef', 'selectedIon', 'sourceFileRef',
            'binaryDataArray', 'analyzer', 'scanSettings',
            'instrumentConfiguration', 'chromatogram', 'target',
            'processingMethod', 'precursor', 'sourceFile',
            'referenceableParamGroup', 'contact', 'scanWindow', 'software'},
        'intlists': {},
        'floatlists': {},
        'charlists': {}}

_pepxml_schema_defaults = {'ints':
    {('xpressratio_summary', 'xpress_light'),
     ('distribution_point', 'obs_5_distr'),
     ('distribution_point', 'obs_2_distr'),
     ('enzymatic_search_constraint', 'max_num_internal_cleavages'),
     ('asapratio_lc_heavypeak', 'right_valley'),
     ('libra_summary', 'output_type'),
     ('distribution_point', 'obs_7_distr'),
     ('spectrum_query', 'index'),
     ('data_filter', 'number'),
     ('roc_data_point', 'num_incorr'),
     ('search_hit', 'num_tol_term'),
     ('search_hit', 'num_missed_cleavages'),
     ('asapratio_lc_lightpeak', 'right_valley'),
     ('libra_summary', 'normalization'),
     ('specificity', 'min_spacing'),
     ('database_refresh_timestamp', 'min_num_enz_term'),
     ('enzymatic_search_constraint', 'min_number_termini'),
     ('xpressratio_result', 'light_lastscan'),
     ('distribution_point', 'obs_3_distr'),
     ('spectrum_query', 'end_scan'),
     ('analysis_result', 'id'),
     ('search_database', 'size_in_db_entries'),
     ('search_hit', 'hit_rank'),
     ('alternative_protein', 'num_tol_term'),
     ('search_hit', 'num_tot_proteins'),
     ('asapratio_summary', 'elution'),
     ('search_hit', 'tot_num_ions'),
     ('error_point', 'num_incorr'),
     ('mixture_model', 'precursor_ion_charge'),
     ('roc_data_point', 'num_corr'),
     ('search_hit', 'num_matched_ions'),
     ('dataset_derivation', 'generation_no'),
     ('xpressratio_result', 'heavy_firstscan'),
     ('xpressratio_result', 'heavy_lastscan'),
     ('error_point', 'num_corr'),
     ('spectrum_query', 'assumed_charge'),
     ('analysis_timestamp', 'id'),
     ('xpressratio_result', 'light_firstscan'),
     ('distribution_point', 'obs_4_distr'),
     ('asapratio_lc_heavypeak', 'left_valley'),
     ('fragment_masses', 'channel'),
     ('distribution_point', 'obs_6_distr'),
     ('affected_channel', 'channel'),
     ('search_result', 'search_id'),
     ('contributing_channel', 'channel'),
     ('asapratio_lc_lightpeak', 'left_valley'),
     ('asapratio_peptide_data', 'area_flag'),
     ('search_database', 'size_of_residues'),
     ('asapratio_peptide_data', 'cidIndex'),
     ('mixture_model', 'num_iterations'),
     ('mod_aminoacid_mass', 'position'),
     ('spectrum_query', 'start_scan'),
     ('asapratio_summary', 'area_flag'),
     ('mixture_model', 'tot_num_spectra'),
     ('search_summary', 'search_id'),
     ('xpressratio_timestamp', 'xpress_light'),
     ('distribution_point', 'obs_1_distr'),
     ('intensity', 'channel'),
     ('asapratio_contribution', 'charge'),
     ('libra_summary', 'centroiding_preference')},
    'floats':
    {('asapratio_contribution', 'error'),
     ('asapratio_lc_heavypeak', 'area_error'),
     ('modification_info', 'mod_nterm_mass'),
     ('distribution_point', 'model_4_neg_distr'),
     ('distribution_point', 'model_5_pos_distr'),
     ('spectrum_query', 'precursor_neutral_mass'),
     ('asapratio_lc_heavypeak', 'time_width'),
     ('xpressratio_summary', 'masstol'),
     ('affected_channel', 'correction'),
     ('distribution_point', 'model_7_neg_distr'),
     ('error_point', 'error'),
     ('intensity', 'target_mass'),
     ('roc_data_point', 'sensitivity'),
     ('distribution_point', 'model_4_pos_distr'),
     ('distribution_point', 'model_2_neg_distr'),
     ('distribution_point', 'model_3_pos_distr'),
     ('mixture_model', 'prior_probability'),
     ('roc_data_point', 'error'),
     ('intensity', 'normalized'),
     ('modification_info', 'mod_cterm_mass'),
     ('asapratio_lc_lightpeak', 'area_error'),
     ('distribution_point', 'fvalue'),
     ('distribution_point', 'model_1_neg_distr'),
     ('peptideprophet_summary', 'min_prob'),
     ('asapratio_result', 'mean'),
     ('point', 'pos_dens'),
     ('fragment_masses', 'mz'),
     ('mod_aminoacid_mass', 'mass'),
     ('distribution_point', 'model_6_neg_distr'),
     ('asapratio_lc_lightpeak', 'time_width'),
     ('asapratio_result', 'heavy2light_error'),
     ('peptideprophet_result', 'probability'),
     ('error_point', 'min_prob'),
     ('peptideprophet_summary', 'est_tot_num_correct'),
     ('roc_data_point', 'min_prob'),
     ('asapratio_result', 'heavy2light_mean'),
     ('distribution_point', 'model_5_neg_distr'),
     ('mixturemodel', 'neg_bandwidth'),
     ('asapratio_result', 'error'),
     ('xpressratio_result', 'light_mass'),
     ('point', 'neg_dens'),
     ('asapratio_lc_lightpeak', 'area'),
     ('distribution_point', 'model_1_pos_distr'),
     ('xpressratio_result', 'mass_tol'),
     ('mixturemodel', 'pos_bandwidth'),
     ('xpressratio_result', 'light_area'),
     ('asapratio_peptide_data', 'heavy_mass'),
     ('distribution_point', 'model_2_pos_distr'),
     ('search_hit', 'calc_neutral_pep_mass'),
     ('intensity', 'absolute'),
     ('asapratio_peptide_data', 'light_mass'),
     ('distribution_point', 'model_3_neg_distr'),
     ('aminoacid_modification', 'mass'),
     ('asapratio_lc_heavypeak', 'time'),
     ('asapratio_lc_lightpeak', 'time'),
     ('asapratio_lc_lightpeak', 'background'),
     ('mixture_model', 'est_tot_correct'),
     ('point', 'value'),
     ('asapratio_lc_heavypeak', 'background'),
     ('terminal_modification', 'mass'),
     ('fragment_masses', 'offset'),
     ('xpressratio_result', 'heavy_mass'),
     ('search_hit', 'protein_mw'),
     ('libra_summary', 'mass_tolerance'),
     ('spectrum_query', 'retention_time_sec'),
     ('distribution_point', 'model_7_pos_distr'),
     ('asapratio_lc_heavypeak', 'area'),
     ('alternative_protein', 'protein_mw'),
     ('asapratio_contribution', 'ratio'),
     ('xpressratio_result', 'heavy_area'),
     ('distribution_point', 'model_6_pos_distr')},
    'bools':
    {('sample_enzyme', 'independent'),
     ('intensity', 'reject'),
     ('libra_result', 'is_rejected')},
    'intlists': set(),
    'floatlists': set(),
    'charlists': set(),
    'lists': {'point', 'aminoacid_modification', 'msms_run_summary',
            'mixturemodel', 'search_hit', 'mixturemodel_distribution',
            'sequence_search_constraint', 'specificity', 'alternative_protein',
            'analysis_result', 'data_filter', 'fragment_masses', 'error_point',
            'parameter', 'spectrum_query', 'search_result', 'affected_channel',
            'analysis_summary', 'roc_data_point', 'distribution_point',
            'search_summary', 'mod_aminoacid_mass', 'search_score', 'intensity',
            'analysis_timestamp', 'mixture_model', 'terminal_modification',
            'contributing_channel', 'inputfile'}}