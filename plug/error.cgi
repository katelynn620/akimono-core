# error �v���O�C�� 2004/01/20 �R��

sub OverLoad
{
	print <<"HTML";
Cache-Control: no-cache, must-revalidate
Pragma: no-cache
Content-type: text/html

<html>
<head>
<title>�ߕ���</title>
</head>
<body>
���݃T�[�o�������׏�Ԃł��B
�\\���󂠂�܂��񂪂��΂炭�A�N�Z�X�������킹�Ă��������B<br>
���דx $_[0] CPUs
</body></html>
HTML
	exit;
}

sub OutError
{
	UnLock() if $LOCKED;
	CoUnLock() if $COLOCKED;
	my %msg=
	(
		"not defined function"=>
			'��`����Ă��Ȃ��֐����Ăяo���܂����B�Ǘ��҂Ɉȉ��̏���A�����Ă��������B<hr>'.
			"not defined function '$_[1]'",
		"busy"=>
			'�A�N�Z�X��<SPAN>���G</SPAN>���Ă���܂��B<br>'.
			'���萔�ł���<SPAN>�K���T�b�ȏ�҂��Ă���</SPAN>�߂��Ă�����x�A�N�Z�X���Ă��������B<br>'.
			($AUTO_UNLOCK_TIME*2).'�b�ȏ�o���Ă��ڑ��ł��Ȃ��ꍇ��'.
			'<a href="mailto:'.$ADMIN_EMAIL.'">�Ǘ��l�܂ł��A��</a>���������B',
		"no data"=>
			'<SPAN>�f�[�^��������܂���ł���</SPAN>�B���萔�ł����߂��Ă�蒼���Ă��������B'.
			'���̃��b�Z�[�W�������ꍇ��<a href="mailto:'.$ADMIN_EMAIL.'">�Ǘ��l�܂ł��A��</a>���������B',
		"stop"=>
			'���̓X�܂�<SPAN>���x�ݒ�</SPAN>�ł��B'.
			'�v���C���ĊJ����Ƃ���<a href="mailto:'.$ADMIN_EMAIL.'">�Ǘ��l�܂ł��A��</a>���������B',
		"no user"=>
			'���݂��Ȃ�ID�ł��BID�����m�F���������B��'.$_[1],
		"incorrect"=>
			'�p�X���[�h���Ԉ���Ă��܂��B���m�F����������'.$_[1],
		"error rename"=>
			'�f�[�^�X�V�Ɏ��s���܂���',
		"timeout"=>
			'���O�C�����璷���Ԃ��o�߂�������<SPAN>�^�C���A�E�g</SPAN>���܂����B<br>���萔�ł���������x�g�b�v���烍�O�C���������Ă��������B',
		"bad request"=>
			'<SPAN>�s���ȌĂяo��</SPAN>�ł��B�u���E�U�́u�߂�/�i�ށv���g���Ă���ꍇ�͎g��Ȃ��悤�ɂ��Ă��������B',
	);
	my $msg=defined $msg{$_[0]} ? $msg{$_[0]} : $_[0];
	$NOMENU=0;$Q{bk}="";
	$disp=<<"HTML";
	<BIG>���G���[���|�[�g</BIG><br><br>
	$msg
HTML
	OutSkin();
	exit;
}

sub WriteErrorLog
{
	eval(<<'__function__');
	my($msg,$file)=@_;
	
	return if !$LOG_SIZE_MAX || $file eq '';
	
	my $fn=GetPath($LOG_DIR,$file);
	rename($fn,GetPath($LOG_DIR,$file."-old")) if (stat($fn))[7]>$LOG_SIZE_MAX;
	open(ERR,">>$fn") or return;
	print ERR
		join("\t",
			(
				$NOW_TIME,
				$ENV{SCRIPT_NAME},
				$ENV{REMOTE_ADDR},
				$ENV{REMOTE_HOST},
				GetTrueIP(),
				$USER,
				$msg,
			)
		)."\n";
	close(ERR);
__function__
}

sub OutErrorBlockLogin
{
	OutError('
		���w���ID��<SPAN>'.$_[0].'</SPAN>�̂��߃A�N�Z�X��������Ă��܂��B<br>
		�v���C���́u�X���v�u���[�U���v�u�X�ܖ��v��Y����<a href="mailto:'.$ADMIN_EMAIL.'">�Ǘ��l�܂ł��A��</a>���������B
	');
}
1;
