#Notepad Input prompt
#seq = numeric - variable
#notepad.prompt(notepad, "msg") prompt for input.
import re
seq = notepad.prompt(notepad, 'Enter Replacement Starting Sequence', 'Reset_Index: y/n, Start_Index: RangeFrom -999 to 9999')

yes_list = ['true', 't', 'y', 'yes','ye','yeah', '+', 'tru', 'positive', '1']

reset_index = str.lower(re.search(r"\S*?\s*?(\S*)\s*?,",seq).group(1))
start_index = int(re.search(r",.*?([+-]?\d+)",seq).group(1))

index_running_seq = 0
policy_running_seq = 0
noreset_index_running_seq = 0

if reset_index in yes_list:
    #policy's index sequence
    def increment_after_indexseq(match):
        global index_running_seq
        index_running_seq += 1
        index_seq = index_running_seq - 1
        return 'edit "{0}"'.format(str(index_seq+start_index))
        #increase starting from 993, replacement starts from 994.
    #sample:edit "107"
    editor.rereplace(r'edit "(\d+)"', increment_after_indexseq)

    #policy's name number seqence 

    def increment_after_policyseq(match):
        global policy_running_seq
        policy_running_seq += 1
        policy_seq = policy_running_seq - 1
        return 'Policy_{0}'.format(str(policy_seq+start_index))
        #increase starting from 993, replacement starts from 994.
    #sample : set name "Policy_1"
    editor.rereplace(r'Policy_(\d+)', increment_after_policyseq)

else:
    
    def increment_after_indexseq(match):
        return 'edit "{0}"'.format(str((int(match.group(1))-1)+int(start_index))) 
        #increase starting from 993, replacement starts from 994.
    #sample:edit "107"
    editor.rereplace(r'edit "(\d+)"', increment_after_indexseq)
    
    #policy's name number seqence 
    def increment_after_policyseq(match):
        global policy_running_seq
        policy_running_seq += 1
        policy_seq = policy_running_seq - 1
        return 'Policy_{0}'.format(str((int(policy_seq)+int(start_index))) 
        #increase starting from 993, replacement starts from 994.
    #sample : set name "Policy_1"
    editor.rereplace(r'Policy_(\d+)', increment_after_policyseq)   