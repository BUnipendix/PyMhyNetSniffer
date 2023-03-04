COMMON_UNIMPORTENT_PACKETS = (
	'PlayerGameTimeNotify',
	'PlayerTimeNotify',
	'WorldPlayerRTTNotify',
	'PlayerSetPauseRsp',
	'PlayerSetPauseReq',
	'PingReq',
	'PingRsp',
	'ServerTimeNotify',
	'SceneTimeNotify',
)
PLAYER_RELATED_PACKETS = (
	'WorldPlayerLocationNotify',
	'AbilityInvocationsNotify',
	'CombatInvocationsNotify',
	'ScenePlayerLocationNotify',
	'ScenePlayerInfoNotify',
	'PlayerPropNotify',
	'AvatarFightPropUpdateNotify',
	'EvtAiSyncSkillCdNotify',
	'EvtDoSkillSuccNotify',
	'EntityFightPropUpdateNotify',
	'EntityFightPropChangeReasonNotify',
	'ClientAbilityInitFinishNotify',
	'ClientAbilityChangeNotify',
	'QueryPathReq',
	'QueryPathRsp'
)
AI_RELATED_UNIMPORTANT_PACKETS = (
	'EvtAiSyncCombatThreatInfoNotify',
	'EntityAiSyncNotify',
)
PROTO_NAME = 'genshin'