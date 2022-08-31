# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActivityInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ActivityWatcherInfo_pb2 as ActivityWatcherInfo__pb2
import ArenaChallengeActivityDetailInfo_pb2 as ArenaChallengeActivityDetailInfo__pb2
import AsterActivityDetailInfo_pb2 as AsterActivityDetailInfo__pb2
import BartenderActivityDetailInfo_pb2 as BartenderActivityDetailInfo__pb2
import BlessingActivityDetailInfo_pb2 as BlessingActivityDetailInfo__pb2
import BlitzRushActivityDetailInfo_pb2 as BlitzRushActivityDetailInfo__pb2
import BounceConjuringActivityDetailInfo_pb2 as BounceConjuringActivityDetailInfo__pb2
import BuoyantCombatDetailInfo_pb2 as BuoyantCombatDetailInfo__pb2
import ChannelerSlabActivityDetailInfo_pb2 as ChannelerSlabActivityDetailInfo__pb2
import ChessActivityDetailInfo_pb2 as ChessActivityDetailInfo__pb2
import CrucibleActivityDetailInfo_pb2 as CrucibleActivityDetailInfo__pb2
import CrystalLinkActivityDetailInfo_pb2 as CrystalLinkActivityDetailInfo__pb2
import DeliveryActivityDetailInfo_pb2 as DeliveryActivityDetailInfo__pb2
import DigActivityDetailInfo_pb2 as DigActivityDetailInfo__pb2
import DragonSpineActivityDetailInfo_pb2 as DragonSpineActivityDetailInfo__pb2
import EchoShellDetailInfo_pb2 as EchoShellDetailInfo__pb2
import EffigyActivityDetailInfo_pb2 as EffigyActivityDetailInfo__pb2
import ExpeditionActivityDetailInfo_pb2 as ExpeditionActivityDetailInfo__pb2
import FindHilichurlDetailInfo_pb2 as FindHilichurlDetailInfo__pb2
import FleurFairActivityDetailInfo_pb2 as FleurFairActivityDetailInfo__pb2
import FlightActivityDetailInfo_pb2 as FlightActivityDetailInfo__pb2
import GachaActivityDetailInfo_pb2 as GachaActivityDetailInfo__pb2
import GearActivityDetailInfo_pb2 as GearActivityDetailInfo__pb2
import GravenInnocenceDetailInfo_pb2 as GravenInnocenceDetailInfo__pb2
import HachiActivityDetailInfo_pb2 as HachiActivityDetailInfo__pb2
import HideAndSeekActivityDetailInfo_pb2 as HideAndSeekActivityDetailInfo__pb2
import InstableSprayDetailInfo_pb2 as InstableSprayDetailInfo__pb2
import IrodoriActivityDetailInfo_pb2 as IrodoriActivityDetailInfo__pb2
import IslandPartyActivityDetailInfo_pb2 as IslandPartyActivityDetailInfo__pb2
import LanternRiteActivityDetailInfo_pb2 as LanternRiteActivityDetailInfo__pb2
import LuminanceStoneChallengeActivityDetailInfo_pb2 as LuminanceStoneChallengeActivityDetailInfo__pb2
import LunaRiteDetailInfo_pb2 as LunaRiteDetailInfo__pb2
import MichiaeMatsuriActivityDetailInfo_pb2 as MichiaeMatsuriActivityDetailInfo__pb2
import MistTrialActivityDetailInfo_pb2 as MistTrialActivityDetailInfo__pb2
import MoonfinTrialActivityDetailInfo_pb2 as MoonfinTrialActivityDetailInfo__pb2
import MuqadasPotionDetailInfo_pb2 as MuqadasPotionDetailInfo__pb2
import MusicGameActivityDetailInfo_pb2 as MusicGameActivityDetailInfo__pb2
import PhotoActivityDetailInfo_pb2 as PhotoActivityDetailInfo__pb2
import PlantFlowerActivityDetailInfo_pb2 as PlantFlowerActivityDetailInfo__pb2
import PotionActivityDetailInfo_pb2 as PotionActivityDetailInfo__pb2
import RogueDiaryActivityDetailInfo_pb2 as RogueDiaryActivityDetailInfo__pb2
import RoguelikeDungeonActivityDetailInfo_pb2 as RoguelikeDungeonActivityDetailInfo__pb2
import SalesmanActivityDetailInfo_pb2 as SalesmanActivityDetailInfo__pb2
import SeaLampActivityDetailInfo_pb2 as SeaLampActivityDetailInfo__pb2
import SeaLampActivityInfo_pb2 as SeaLampActivityInfo__pb2
import SpiceActivityDetailInfo_pb2 as SpiceActivityDetailInfo__pb2
import SummerTimeDetailInfo_pb2 as SummerTimeDetailInfo__pb2
import SummerTimeV2DetailInfo_pb2 as SummerTimeV2DetailInfo__pb2
import SumoActivityDetailInfo_pb2 as SumoActivityDetailInfo__pb2
import TanukiTravelActivityDetailInfo_pb2 as TanukiTravelActivityDetailInfo__pb2
import TreasureMapActivityDetailInfo_pb2 as TreasureMapActivityDetailInfo__pb2
import TreasureSeelieDetailInfo_pb2 as TreasureSeelieDetailInfo__pb2
import TrialAvatarActivityDetailInfo_pb2 as TrialAvatarActivityDetailInfo__pb2
import UgcActivityDetailInfo_pb2 as UgcActivityDetailInfo__pb2
import Unk2800_PHPHMILPOLC_pb2 as Unk2800__PHPHMILPOLC__pb2
import WaterSpiritActivityDetailInfo_pb2 as WaterSpiritActivityDetailInfo__pb2
import WinterCampActivityDetailInfo_pb2 as WinterCampActivityDetailInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x41\x63tivityInfo.proto\x1a\x19\x41\x63tivityWatcherInfo.proto\x1a&ArenaChallengeActivityDetailInfo.proto\x1a\x1d\x41sterActivityDetailInfo.proto\x1a!BartenderActivityDetailInfo.proto\x1a BlessingActivityDetailInfo.proto\x1a!BlitzRushActivityDetailInfo.proto\x1a\'BounceConjuringActivityDetailInfo.proto\x1a\x1d\x42uoyantCombatDetailInfo.proto\x1a%ChannelerSlabActivityDetailInfo.proto\x1a\x1d\x43hessActivityDetailInfo.proto\x1a CrucibleActivityDetailInfo.proto\x1a#CrystalLinkActivityDetailInfo.proto\x1a DeliveryActivityDetailInfo.proto\x1a\x1b\x44igActivityDetailInfo.proto\x1a#DragonSpineActivityDetailInfo.proto\x1a\x19\x45\x63hoShellDetailInfo.proto\x1a\x1e\x45\x66\x66igyActivityDetailInfo.proto\x1a\"ExpeditionActivityDetailInfo.proto\x1a\x1d\x46indHilichurlDetailInfo.proto\x1a!FleurFairActivityDetailInfo.proto\x1a\x1e\x46lightActivityDetailInfo.proto\x1a\x1dGachaActivityDetailInfo.proto\x1a\x1cGearActivityDetailInfo.proto\x1a\x1fGravenInnocenceDetailInfo.proto\x1a\x1dHachiActivityDetailInfo.proto\x1a#HideAndSeekActivityDetailInfo.proto\x1a\x1dInstableSprayDetailInfo.proto\x1a\x1fIrodoriActivityDetailInfo.proto\x1a#IslandPartyActivityDetailInfo.proto\x1a#LanternRiteActivityDetailInfo.proto\x1a/LuminanceStoneChallengeActivityDetailInfo.proto\x1a\x18LunaRiteDetailInfo.proto\x1a&MichiaeMatsuriActivityDetailInfo.proto\x1a!MistTrialActivityDetailInfo.proto\x1a$MoonfinTrialActivityDetailInfo.proto\x1a\x1dMuqadasPotionDetailInfo.proto\x1a!MusicGameActivityDetailInfo.proto\x1a\x1dPhotoActivityDetailInfo.proto\x1a#PlantFlowerActivityDetailInfo.proto\x1a\x1ePotionActivityDetailInfo.proto\x1a\"RogueDiaryActivityDetailInfo.proto\x1a(RoguelikeDungeonActivityDetailInfo.proto\x1a SalesmanActivityDetailInfo.proto\x1a\x1fSeaLampActivityDetailInfo.proto\x1a\x19SeaLampActivityInfo.proto\x1a\x1dSpiceActivityDetailInfo.proto\x1a\x1aSummerTimeDetailInfo.proto\x1a\x1cSummerTimeV2DetailInfo.proto\x1a\x1cSumoActivityDetailInfo.proto\x1a$TanukiTravelActivityDetailInfo.proto\x1a#TreasureMapActivityDetailInfo.proto\x1a\x1eTreasureSeelieDetailInfo.proto\x1a#TrialAvatarActivityDetailInfo.proto\x1a\x1bUgcActivityDetailInfo.proto\x1a\x19Unk2800_PHPHMILPOLC.proto\x1a#WaterSpiritActivityDetailInfo.proto\x1a\"WinterCampActivityDetailInfo.proto\"\x92\x1f\n\x0c\x41\x63tivityInfo\x12\x19\n\x11is_play_open_anim\x18\r \x01(\x08\x12\x13\n\x0bschedule_id\x18\x0f \x01(\r\x12\x12\n\tcur_score\x18\xf2\x0e \x01(\r\x12\x13\n\x0bis_starting\x18\t \x01(\x08\x12\x1a\n\x11taken_reward_list\x18\xc9\x02 \x03(\r\x12\x1b\n\x13Unk2700_NONJFHAIFLA\x18\x66 \x01(\x08\x12\"\n\x19selected_avatar_reward_id\x18\x8a\n \x01(\r\x12\x1d\n\x14\x66irst_day_start_time\x18\xd0\x04 \x01(\r\x12\x14\n\x0bscore_limit\x18\xa6\x0f \x01(\r\x12\x13\n\x0bis_finished\x18\x06 \x01(\x08\x12\x12\n\tis_hidden\x18\x97\x07 \x01(\x08\x12\x12\n\nbegin_time\x18\x08 \x01(\r\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\r\x12>\n\x11\x61\x63tivity_coin_map\x18\xaa\x05 \x03(\x0b\x32\".ActivityInfo.ActivityCoinMapEntry\x12\x15\n\ractivity_type\x18\x04 \x01(\r\x12\x1c\n\x13Unk2700_EDKLLHBEEGE\x18\xa9\x0b \x01(\x08\x12\x32\n\x13Unk2800_KOMIPKKKOBE\x18\xe0\x06 \x03(\x0b\x32\x14.Unk2800_PHPHMILPOLC\x12\x16\n\x0emeet_cond_list\x18\n \x03(\r\x12\x43\n\x13Unk2700_IFPBCNLCKLG\x18\xf7\n \x03(\x0b\x32%.ActivityInfo.Unk2700IFPBCNLCKLGEntry\x12\x18\n\x10\x65xpire_cond_list\x18\x03 \x03(\r\x12/\n\x11watcher_info_list\x18\x02 \x03(\x0b\x32\x14.ActivityWatcherInfo\x12\x13\n\x0b\x61\x63tivity_id\x18\x0c \x01(\r\x12\x33\n\rsam_lamp_info\x18\x07 \x01(\x0b\x32\x1a.SeaLampActivityDetailInfoH\x00\x12\x34\n\rcrucible_info\x18\x0e \x01(\x0b\x32\x1b.CrucibleActivityDetailInfoH\x00\x12\x34\n\rsalesman_info\x18\x0b \x01(\x0b\x32\x1b.SalesmanActivityDetailInfoH\x00\x12;\n\x11trial_avatar_info\x18\x01 \x01(\x0b\x32\x1e.TrialAvatarActivityDetailInfoH\x00\x12\x35\n\rdelivery_info\x18\xc4\x08 \x01(\x0b\x32\x1b.DeliveryActivityDetailInfoH\x00\x12/\n\naster_info\x18\xad\x04 \x01(\x0b\x32\x18.AsterActivityDetailInfoH\x00\x12\x31\n\x0b\x66light_info\x18\xd5\n \x01(\x0b\x32\x19.FlightActivityDetailInfoH\x00\x12<\n\x11\x64ragon_spine_info\x18\xbf\r \x01(\x0b\x32\x1e.DragonSpineActivityDetailInfoH\x00\x12\x31\n\x0b\x65\x66\x66igy_info\x18\x87\x03 \x01(\x0b\x32\x19.EffigyActivityDetailInfoH\x00\x12<\n\x11treasure_map_info\x18\xda\x08 \x01(\x0b\x32\x1e.TreasureMapActivityDetailInfoH\x00\x12\x35\n\rblessing_info\x18\xcd\x0e \x01(\x0b\x32\x1b.BlessingActivityDetailInfoH\x00\x12.\n\rsea_lamp_info\x18\xee\x03 \x01(\x0b\x32\x14.SeaLampActivityInfoH\x00\x12\x39\n\x0f\x65xpedition_info\x18\xca\x01 \x01(\x0b\x32\x1d.ExpeditionActivityDetailInfoH\x00\x12\x42\n\x14\x61rena_challenge_info\x18\xdb\x06 \x01(\x0b\x32!.ArenaChallengeActivityDetailInfoH\x00\x12\x38\n\x0f\x66leur_fair_info\x18\xd9\x06 \x01(\x0b\x32\x1c.FleurFairActivityDetailInfoH\x00\x12<\n\x11water_spirit_info\x18\x8b\r \x01(\x0b\x32\x1e.WaterSpiritActivityDetailInfoH\x00\x12@\n\x13\x63hanneler_slab_info\x18\xf7\x07 \x01(\x0b\x32 .ChannelerSlabActivityDetailInfoH\x00\x12\x41\n\x18mist_trial_activity_info\x18\x9c\x01 \x01(\x0b\x32\x1c.MistTrialActivityDetailInfoH\x00\x12=\n\x12hide_and_seek_info\x18\xab\x03 \x01(\x0b\x32\x1e.HideAndSeekActivityDetailInfoH\x00\x12\x38\n\x13\x66ind_hilichurl_info\x18\x83\x0b \x01(\x0b\x32\x18.FindHilichurlDetailInfoH\x00\x12\x32\n\x10summer_time_info\x18\xdc\n \x01(\x0b\x32\x15.SummerTimeDetailInfoH\x00\x12\x38\n\x13\x62uoyant_combat_info\x18\xb2\x0e \x01(\x0b\x32\x18.BuoyantCombatDetailInfoH\x00\x12\x30\n\x0f\x65\x63ho_shell_info\x18\xd9\x08 \x01(\x0b\x32\x14.EchoShellDetailInfoH\x00\x12\x44\n\x15\x62ounce_conjuring_info\x18\xff\x05 \x01(\x0b\x32\".BounceConjuringActivityDetailInfoH\x00\x12\x38\n\x0f\x62litz_rush_info\x18\x9a\x06 \x01(\x0b\x32\x1c.BlitzRushActivityDetailInfoH\x00\x12/\n\nchess_info\x18\x9f\x07 \x01(\x0b\x32\x18.ChessActivityDetailInfoH\x00\x12-\n\tsumo_info\x18\xed\t \x01(\x0b\x32\x17.SumoActivityDetailInfoH\x00\x12>\n\x12moonfin_trial_info\x18\xb4\x0c \x01(\x0b\x32\x1f.MoonfinTrialActivityDetailInfoH\x00\x12.\n\x0eluna_rite_info\x18\xae\x06 \x01(\x0b\x32\x13.LunaRiteDetailInfoH\x00\x12;\n\x11plant_flower_info\x18\x36 \x01(\x0b\x32\x1e.PlantFlowerActivityDetailInfoH\x00\x12\x38\n\x0fmusic_game_info\x18\xcc\x03 \x01(\x0b\x32\x1c.MusicGameActivityDetailInfoH\x00\x12\x46\n\x16roguelike_dungeon_info\x18\xdb\x01 \x01(\x0b\x32#.RoguelikeDungeonActivityDetailInfoH\x00\x12+\n\x08\x64ig_info\x18\x93\x03 \x01(\x0b\x32\x16.DigActivityDetailInfoH\x00\x12/\n\nhachi_info\x18\xeb\x03 \x01(\x0b\x32\x18.HachiActivityDetailInfoH\x00\x12:\n\x10winter_camp_info\x18\xbb\x08 \x01(\x0b\x32\x1d.WinterCampActivityDetailInfoH\x00\x12\x31\n\x0bpotion_info\x18\xf9\t \x01(\x0b\x32\x19.PotionActivityDetailInfoH\x00\x12G\n\x1btanuki_travel_activity_info\x18\x84\x0e \x01(\x0b\x32\x1f.TanukiTravelActivityDetailInfoH\x00\x12\x45\n\x1alantern_rite_activity_info\x18\xd4\x0e \x01(\x0b\x32\x1e.LanternRiteActivityDetailInfoH\x00\x12\x42\n\x14michiae_matsuri_info\x18\xc2\x01 \x01(\x0b\x32!.MichiaeMatsuriActivityDetailInfoH\x00\x12\x37\n\x0e\x62\x61rtender_info\x18\xbd\r \x01(\x0b\x32\x1c.BartenderActivityDetailInfoH\x00\x12+\n\x08ugc_info\x18\xbf\x05 \x01(\x0b\x32\x16.UgcActivityDetailInfoH\x00\x12<\n\x11\x63rystal_link_info\x18\xca\t \x01(\x0b\x32\x1e.CrystalLinkActivityDetailInfoH\x00\x12\x33\n\x0cirodori_info\x18\xee\x05 \x01(\x0b\x32\x1a.IrodoriActivityDetailInfoH\x00\x12/\n\nphoto_info\x18\xc8\x02 \x01(\x0b\x32\x18.PhotoActivityDetailInfoH\x00\x12/\n\nspice_info\x18\xe3\x0e \x01(\x0b\x32\x18.SpiceActivityDetailInfoH\x00\x12/\n\ngacha_info\x18\xb9\x06 \x01(\x0b\x32\x18.GachaActivityDetailInfoH\x00\x12U\n\x1eluminance_stone_challenge_info\x18\x9c\n \x01(\x0b\x32*.LuminanceStoneChallengeActivityDetailInfoH\x00\x12:\n\x10rogue_diary_info\x18\xac\x06 \x01(\x0b\x32\x1d.RogueDiaryActivityDetailInfoH\x00\x12\x37\n\x13summer_time_v2_info\x18\xee\x04 \x01(\x0b\x32\x17.SummerTimeV2DetailInfoH\x00\x12<\n\x11island_party_info\x18\xdd\x0e \x01(\x0b\x32\x1e.IslandPartyActivityDetailInfoH\x00\x12-\n\tgear_info\x18\xd2\x05 \x01(\x0b\x32\x17.GearActivityDetailInfoH\x00\x12<\n\x15graven_innocence_info\x18\xf7\x0e \x01(\x0b\x32\x1a.GravenInnocenceDetailInfoH\x00\x12\x38\n\x13instable_spray_info\x18\x93\x08 \x01(\x0b\x32\x18.InstableSprayDetailInfoH\x00\x12\x38\n\x13muqadas_potion_info\x18\x85\t \x01(\x0b\x32\x18.MuqadasPotionDetailInfoH\x00\x12:\n\x14treasure_seelie_info\x18\xc6\x07 \x01(\x0b\x32\x19.TreasureSeelieDetailInfoH\x00\x1a\x36\n\x14\x41\x63tivityCoinMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17Unk2700IFPBCNLCKLGEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x08\n\x06\x64\x65tailb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ActivityInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACTIVITYINFO_ACTIVITYCOINMAPENTRY._options = None
  _ACTIVITYINFO_ACTIVITYCOINMAPENTRY._serialized_options = b'8\001'
  _ACTIVITYINFO_UNK2700IFPBCNLCKLGENTRY._options = None
  _ACTIVITYINFO_UNK2700IFPBCNLCKLGENTRY._serialized_options = b'8\001'
  _ACTIVITYINFO._serialized_start=1949
  _ACTIVITYINFO._serialized_end=5935
  _ACTIVITYINFO_ACTIVITYCOINMAPENTRY._serialized_start=5812
  _ACTIVITYINFO_ACTIVITYCOINMAPENTRY._serialized_end=5866
  _ACTIVITYINFO_UNK2700IFPBCNLCKLGENTRY._serialized_start=5868
  _ACTIVITYINFO_UNK2700IFPBCNLCKLGENTRY._serialized_end=5925
# @@protoc_insertion_point(module_scope)