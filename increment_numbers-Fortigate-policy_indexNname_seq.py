#Notepad Input prompt
#seq = numeric - variable
#notepad.prompt(notepad, "msg") prompt for input.

seq = notepad.prompt(notepad, 'Enter Replacement Starting Sequence', 'from -999 to 0 to 9999')

start_index = seq

index_running_seq = 0
policy_running_seq = 0

#policy's index sequence
def increment_after_indexseq(match):
    global index_running_seq
    index_running_seq += 1
    index_seq = index_running_seq -1
    return 'edit "{0}"'.format(str(int(index_seq)+int(start_index)))
    #increase starting from 993, replacement starts from 994.
#sample:edit "107"

#policy's name number seqence 
def increment_after_nameseq(match):
    global policy_running_seq
    policy_running_seq += 1
    policy_seq = policy_running_seq -1
    return 'Policy_{0}'.format(str(int(policy_seq)+int(start_index)))
    
    #increase starting from 993, replacement starts from 994.
#sample : set name "Policy_1"


editor.rereplace(r'edit "(\d+)"', increment_after_indexseq)

editor.rereplace(r'Policy_(\d+)', increment_after_nameseq)

