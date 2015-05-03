from tests.ReqTracer import Requirements

from nose2.events import Plugin

class ReqTrace(Plugin):
    configSection = 'reqtrace'
    commandLineSwitch = ('R', 'reqtrace', 'Requirements tracing')

    def afterSummaryReport(self, event):
        with open('reqtrace.txt', 'w+') as f:
            for req in sorted(Requirements, key=lambda key: Requirements[key]):
                f.write(req+' '+','.join(Requirements[req].func_name)+'\n')
            else:
                print('Wrote tested requirements and their tests to reqtrace.txt\n')