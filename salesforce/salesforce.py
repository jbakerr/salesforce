from salesforce_reporting import Connection, ReportParser
import pandas as pd 


def load_report(report_id, sf):
    report = sf.get_report(report_id)
    parser = ReportParser(report)
    report = parser.records_dict()
    report = pd.DataFrame(report)
    return report