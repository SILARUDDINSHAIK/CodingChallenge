import pandas as pd


# Method to generate first sns topic data
def firsttopicdata(attempts, received):
    # Finding cummulative count of each moduleid(attempt) based on timestamps
    result = (
        attempts.groupby(['moduleid', 'timestamp'])
            .size()
            .groupby('moduleid')
            .apply(lambda s: s.cumsum() - s)
            .to_frame('tx_attempts')
            .merge(attempts, how='right', left_index=True, right_on=['moduleid', 'timestamp'])

    )
    # Event generated data with cumulative attempts
    snsdata = pd.merge(result, received,
                       how='inner', on=['moduleid', 'timestamp'])
    snsdata = snsdata[['moduleid', 'timestamp', 'tx_attempts']]
    snsdata.tx_attempts += 1
    snsdata.index += 1
    snsdata = snsdata.sort_values(by='timestamp', ascending=True)
    #print(snsdata)
    return snsdata


# Method to generate  weekly diagnostic data
def weeklydiagnosticdata(received):
    received["week_no"] = pd.to_datetime(received["timestamp"]).dt.isocalendar().week
    diagnosticdata = (
        received
            .groupby(['week_no', 'moduleid', 'timestamp'])
            .sum()
            .reset_index()
    )
    del diagnosticdata['week_no']
    return diagnosticdata


# Method to define success rate
def SuccessPercentage(attemptdata, receiveddata):
    # left outer join
    successdata = pd.merge(attemptdata, receiveddata,
                           how='left', on=['moduleid', 'timestamp'])
    successdata = (successdata.fillna(0))
    successdata['received_x'] = successdata['received_x'].astype(float)
    successdata['success_rate'] = (successdata['received_y'] / successdata['received_x']) * 100
    return successdata


def main():
    attempts = pd.read_json('attempts.json', lines=True)
    attempts.index += 1
    #print(attempts.tail(40))
    received = pd.read_json('received.json', lines=True)
    received.index += 1
    #print(received)
    snsdata = firsttopicdata(attempts, received)
    snsdata.to_json('Data/FirstSnsData.json', orient='records', lines=True)
    diagnosticdata = weeklydiagnosticdata(received)
    diagnosticdata.to_json('Data/WeeklyDiagnosticData.json', orient='records', lines=True)
    successdata = SuccessPercentage(attempts, received)
    successdata=successdata[['moduleid','timestamp','success_rate']]
    successdata.to_json('Data/SuccessRateDetails.json', orient='records', lines=True)


main()
