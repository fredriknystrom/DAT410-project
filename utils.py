from IPython.core.display import display_html, HTML

def scroll_df(df, max_height=300, max_width=1000):
    display_html(HTML(f"""
        <div style="
            overflow: auto;
            max-height: {max_height}px;
            max-width: {max_width}px;
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px;
        ">
            {df.to_html()}
        </div>"""))


def calculate_class(in_study_repair, time_step, length_of_study_time_step):
    """
    The classes 0, 1, 2, 3, 4 are related to readouts within a time window of: (more than 48), (48 to 24), (24 to 12), (12
    to 6), and (6 to 0) time_step before the failure. If in_study_repair is = 0 then class 0.
    """

    if in_study_repair == 0:
        return 0
    
    remaining_time = length_of_study_time_step - time_step

    if remaining_time > 48:
        return 0
    elif 48 >= remaining_time > 24:
        return 1
    elif 24 >= remaining_time > 12:
        return 2
    elif 12 >= remaining_time > 6:
        return 3
    else:  # remaining_time <= 6
        return 4