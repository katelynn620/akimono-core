# �f���������ݏ��� 2003/09/25 �R��

if ($Q{message} eq "" || $Q{message} =~ /^(\x81\x40|\s|<br>)+$/)
	{ OutError("���b�Z�[�W�����͂���Ă��܂���B"); }
if ($Q{sub} eq "" || $Q{sub} =~ /^(\x81\x40|\s)+$/)
	{ OutError("�^�C�g�������͂���Ă��܂���B"); }

# �Ǘ��ҔF��
$Q{name}=$adminname,$Q{town}="" 	if ($MASTER_USER);

# ���O�t�@�C���ǂݍ���
open(IN,$datafile);
@lines = <IN>;
close(IN);

# �L��no.
$top = shift(@lines);
($count,$ip,$tim) = split(/<>/, $top);
if ($count % 9999) { $count++; } else { $count=1; }

	# �e�L��
	if ($Q{no} eq 'new') {
		unshift (@lines,"$count<>no<>0<>$Q{sub}<>$Q{town}<>$Q{name}<>$Q{message}<>$NOW_TIME<>$host<>$count<>$Q{smail}<>0<>\n");
		@new = @lines;
	}
	# ���X�L��
	else {
		# ���X�̂����c���[�Ƃ����łȂ��c���[�𕪊�
		@new=();	# �グ����c���[
		@tmp=();	# �c��c���[
		$flag=0;
		foreach (@lines) {
			chop;
			($no,$reno,$lx,$t,$e,$n,$m,$tm,$h,$OYA,$smail,$res) = split(/<>/);
			if ($flag == 1 && $lx2 > $lx && $OYA == $Q{oya}) {
				$flag=2;	#���̂܂܂�����
				push(@new,"$count<>$Q{no}<>$lx2<>$Q{sub}<>$Q{town}<>$Q{name}<>$Q{message}<>$NOW_TIME<>$host<>$Q{oya}<>$Q{smail}<>0<>\n");
			}
			if ($no == $Q{no}) {
				$res++;
			push(@new,"$no<>$reno<>$lx<>$t<>$e<>$n<>$m<>$tm<>$h<>$OYA<>$smail<>$res<>\n");
				}
			elsif ($Q{oya} == $OYA) { push(@new,"$_\n"); }
			else { push(@tmp,"$_\n"); }
				if ($no == $Q{no}) {
				$flag=1;
				$lx2 = $lx + 1;
			}
		}
		if ($flag != 2) {
			#�Ō�ɂ�����
			push(@new,"$count<>$Q{no}<>$lx2<>$Q{sub}<>$Q{town}<>$Q{name}<>$Q{message}<>$NOW_TIME<>$host<>$Q{oya}<>$Q{smail}<>0<>\n");
		}
		push(@new,@tmp);
	}
	# �ő�L��������
	if (@new > $max) {
		foreach (0 .. $#new) {
			my($p_file) = pop(@new);
			local($no,$reno,$lx) = split(/<>/, $p_file);
			if ($#new+1 <= $max && $reno eq 'no') {
				last;
				}
		}
	}

	unshift(@new,"$count<>$addr<>$NOW_TIME<>\n");
	OpenAndCheck(GetPath($COTEMP_DIR,'treelog'));
	print OUT @new;
	close(OUT);
	CoDataCA();
	CoUnLock();

	$disp.="�������݂��������܂����B --".GetMenuTag('treebbs','[�L���ꗗ�ɖ߂�]');
1;