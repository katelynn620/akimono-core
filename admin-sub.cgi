# �ʃ��[�U�[�Ǘ� 2005/03/30 �R��

require $JCODE_FILE;
Lock();
DataRead();
CheckUserPass();
OutError('') if !$MASTER_USER || $USER ne 'soldoutadmin';

OutError('���[�U��������܂���') if !defined($name2idx{$Q{user}});
my $DT=$DT[$name2idx{$Q{user}}];

$Q{comment}="�y".jcode::sjis($Q{comment})."�z" if $Q{comment} ne '';

#�d���o�^�����A�N�Z�X�����̌ʑΉ�
if($Q{nocheckip})
{
	$disp.='�d���o�^�`�F�b�N�ΏۊO�Ƃ��܂���',$DT->{nocheckip}=1 if $Q{nocheckip} eq 'nocheck';
	$disp.='�d���o�^�`�F�b�N�ΏۂƂ��܂���',$DT->{nocheckip}='' if $Q{nocheckip} eq 'check';
}

#�A�N�Z�X��������
if($Q{blocklogin})
{
	$Q{blocklogin}=jcode::sjis($Q{blocklogin});
	if($Q{blocklogin} eq 'off')
	{
		$disp.='�A�N�Z�X�������������܂���';
		$DT->{blocklogin}='';
		$DT->{lastlogin}=$NOW_TIME;
	}
	elsif($Q{blocklogin} eq 'stop')
	{
		$disp.='�o�c�x�~�ɐݒ肵�܂���['.$Q{blocklogin}.']';
		$DT->{blocklogin}=$Q{blocklogin};
	}
	elsif($Q{blocklogin} ne '')
	{
		$disp.='�A�N�Z�X���������܂���['.$Q{blocklogin}.']';
		$DT->{blocklogin}=$Q{blocklogin};
	}
}

#�Ǖ�
if($Q{closeshop} eq 'closeshop')
{
	CloseShop($DT->{id},'�Ǖ�');
	PushLog(1,0,"$Q{comment}$DT->{shopname}�͒Ǖ�����܂����B") if (!$Q{log});

	$disp.="�Ǖ�����";
	$DTblockip=$DT->{remoteaddr};
}

#�ܕi���^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{senditem})
{
	my $itemno=$Q{senditem};
	my $ITEM=$ITEM[$itemno];
	my $itemcount=$Q{count};
	$itemcount+=$DT->{item}->[$itemno-1];
	$itemcount=$ITEM->{limit} if $itemcount>$ITEM[$itemno]->{limit};
	$DT->{item}->[$itemno-1]=$itemcount;
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}��$ITEM->{name}�������܂����B") if $Q{comment};
	$disp.="$ITEM->{name} $Q{count}$ITEM->{scale} �ܕi���^����";
}

#�܋����^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{sendmoney})
{
	$DT->{money}+=$Q{sendmoney};
	#$DT->{saletoday}+=$Q{sendmoney};
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}�ɏ܋��������܂����B") if $Q{comment};
	$disp.=GetMoneyString($Q{sendmoney})." �܋����^����";
}

#�������Ԏ��^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{sendtime})
{
	$disp.=$Q{sendtime}."���� �������Ԏ��^����";
	$Q{sendtime}=$Q{sendtime} * 3600;
	$DT->{time}-=$Q{sendtime};
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}�Ɂu".GetTime2HMS($Q{sendtime})."�v�������܂����B") if $Q{comment};
}

#�݈ʎ��^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{senddig})
{
	$disp.=$Q{senddig}."�|�C���g �݈ʌo���l���^����";
	$DT->{dignity}+=$Q{senddig};
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}�Ɏ݈ʌo���l".($Q{senddig}+0)."�|�C���g�������܂����B") if $Q{comment};
}

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp="�s�����������Ƃ��̃p�����[�^�𐳂����I��/�L�q���Ă�������" if $disp eq '';
$disp.=" <-- $DT->{shopname} [$DT->{name}] $Q{comment}";

$NOMENU=1;
$Q{bk}="none";
OutSkin();
1;
