import dataprocess


if __name__ == '__main__':
    args = dataprocess.parse_input_arguments()

    top_occupation_results, top_state_results, total_status_count = dataprocess.get_topk_metrics(args,
                                                                     occupation_column_name="SOC_NAME",
                                                                     state_column_name="WORKSITE_STATE",
                                                                     status_column_name="CASE_STATUS",
                                                                     status_value="CERTIFIED")
    # metrics for top 10 occupations
    dataprocess.output_data(args=args, output_file_path = args.output_file_occupations,
                            top_k_results=top_occupation_results,
                            total_status_count=total_status_count,
                            output_columns=['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'])

    # metrics for top 10 states
    dataprocess.output_data(args=args, output_file_path = args.output_file_states, top_k_results=top_state_results,
                            total_status_count=total_status_count,
                            output_columns = ['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'])



