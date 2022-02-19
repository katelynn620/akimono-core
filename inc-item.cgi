# �A�C�e���֐� 2005/01/06 �R��

package item; #�ύX�s��

######################################################################
# ���A�C�e���p�����֐��F���O��������
# usage: WriteLog(�d�v�x,�ΏۓX��ID,���b�Z�[�W)
#           �d�v�x     0==��� 1==�d�v
#           �ΏۓX��ID 0==�S�X�܈� �X��ID==�v���C�x�[�g
#           ���b�Z�[�W ���O���b�Z�[�W
# return: 0 �Œ�
######################################################################
sub WriteLog
{
	main::PushLog($_[0],$_[1],$_[2]);
	return 0;
}

######################################################################
# ���f�o�b�O�p���O��������
# usage: DebugLog(���b�Z�[�W)
#           ���b�Z�[�W ���O���b�Z�[�W
# return: 0 �Œ�
######################################################################
sub DebugLog
{
	my($msg)=@_;
	main::WriteErrorLog($msg,$main::LOG_DEBUG_FILE) if $main::DEBUG_LOG_ENABLE;
	return 0;
}

######################################################################
# ���A�C�e���p�����֐��F�A�C�e������
# usage: UseItem(�A�C�e���ԍ�,�����,���b�Z�[�W)
#           �A�C�e���ԍ� 1~
#           �����     1~
#           ���b�Z�[�W   �\�����b�Z�[�W
# return: 0 �Œ�
######################################################################
sub UseItem
{
	my($itemno,$count,$msg)=@_;

	$count=UseItemSub($itemno,$count,$DT);
	push(@{$USE->{result}->{useitem}},[$itemno,$count]);
	push(@{$USE->{result}->{usemsg}},$msg);
	return 0;
}
sub UseItemSub
{
	my($itemno,$count,$DT)=@_;
	
	$count=$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]<$count;
	$DT->{item}[$itemno-1]-=$count;
	
	return $count;
}

######################################################################
# ���A�C�e���p�����֐��F�A�C�e���擾
# usage: AddItem(�A�C�e���ԍ�,�擾��,���b�Z�[�W)
#           �A�C�e���ԍ� 1~
#           �擾��     1~
#           ���b�Z�[�W   �\�����b�Z�[�W
# return: 0 �Œ�
######################################################################
sub AddItem
{
	my($itemno,$count,$msg)=@_;

	$count=AddItemSub($itemno,$count,$DT);
	push(@{$USE->{result}->{additem}},[$itemno,$count]);
	push(@{$USE->{result}->{addmsg}},$msg);
	return 0;
}
sub AddItemSub
{
	my($itemno,$count,$DT)=@_;
	
	$count=$main::ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $main::ITEM[$itemno]->{limit}<$DT->{item}[$itemno-1]+$count;
	$DT->{item}[$itemno-1]+=$count;
	
	return $count;
}

sub GetUserData
{
	return &main::GetUserData;
}

sub GetMoneyString
{
	return &main::GetMoneyString;
}

require "$main::ITEM_DIR/funcitem.cgi" if $main::DEFINE_FUNCITEM;
1;
