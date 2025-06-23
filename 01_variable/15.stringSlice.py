# 15 문자열, slice, id, is

# 문자열을 slice한 결과 id 및 is 연산자 출력결과를 확인하라
#
# 문자열
t = 'korea'

# 슬라이스 및 id 출력
# print( t, id(t), '--\n', t[:1],id(t[:1]), ' --\n', t[:2],id(t[:2]), ' --\n', t[:3],id(t[:3]), ' --\n', t[:4],id(t[:4]))
# korea,
# t,
# ko,
# kor,
# kore,
# korea, 메모리는 다 같음
# print( t, id(t[:]) )
# ??

# is 연산자 결과
print( 't is t[:] = ', t is t[:] ) #true
print( 't is t[:1] = ', t is t[:1] ) #true
print( 't[:1] is t[:2] = ', t[:1] is t[:2] )#true
print( 't[:] is t[:5] = ', t[:] is t[:5] )#true
