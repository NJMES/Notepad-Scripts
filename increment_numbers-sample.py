
#rule's index
#def increment_after_openparen(match):
    #return 'edit "{0}"'.format(str(int(match.group(1))+993)) #increase starting from 993
#sample:edit "107"
#editor.rereplace(r'edit "(\d+)"', increment_after_openparen)

#policy number 
def increment_after_openparen(match):
    return 'Policy_{0}'.format(str(int(match.group(1))+993)) #increase starting from 993

#sample : Policy_1
editor.rereplace(r'Policy_(\d+)', increment_after_openparen)
