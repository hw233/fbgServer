# -*- coding: utf-8 -*-
__author__ = 'chongxin'


class LotteryError:
    Fail = 3
    Success=0
    Money_not_enough =1
    Diamond_not_enough = 2

class FriendError:
    # 玩家不存在
    Player_not_exist = 1
    # 请输入正确的ID
    Pls_input_correct_Id = 2
    # 玩家列表已满
    Friend_list_is_full = 3
    # 已经是好友
    Friend_already_is_friend = 4
    # 在黑名单中
    Friend_he_is_in_black = 5
    # 没有申请过
    Friend_has_not_apply = 6
    # 不是好友不能加黑名单
    Friend_is_not_friend = 7
    # 已经在黑名单
    Friend_already_in_black = 8

class BodyPowerEroor:
    # 没有购买次数
    has_not_enough_buy_times = 1
    # 没有足够的钻石
    has_not_enough_diamond = 2

class ChatError:
    # 消息超过规定长度
    Chat_message_is_overflow = 1
    # 世界频道等级不够
    Chat_world_level_not_enough = 2
    # 世界频道CD
    Chat_world_cd = 3

    # 玩家不在线
    Chat_player_offline = 4
    # 没有足够的钻石
    has_not_enough_diamond = 5
    # 不文明发言
    has_bad_words = 6

class PieceCombineError:
    # 碎片不存在
    Piece_not_exist = 1
    # 碎片不够
    Piece_not_enough = 2
class DiamondModuleError:
    # 宝石不存在
    Diamond_not_exist = 1
    # 宝石不够
    Diamond_not_enough = 2
    # 宝石已经镶嵌
    Diamond_exist = 3
    # 宝石未开槽
    Diamond_hold_not_open =4
    # 宝石开槽材料不足
    Diamond_not_material = 5
    # 宝石已经开槽
    Diamond_exist_hold = 6
    # 宝石合成材料不足
    Diamond_compound_not_material = 7
    # 宝石不可合成
    Diamond_not_compound = 8

class EquipModuleError:
    # 装备不存在
    Equip_not_exist = 1
    # 装备不够
    Equip_not_enough = 2
    # 材料不足
    Equip_make_material_not_enough = 3

    # 扣除道具失败
    Equip_dec_item_fail = 4
    # 欧元不够
    Equip_not_euro_enough = 5
    # 传承装备强化等级不够
    Equip_not_strong_enough = 6



class GiftModuleError:
    # 礼包不存在
    Gift_not_exist = 1
    # 礼包不够
    Gift_not_enough = 2
    # 操作数据库出错
    Gift_db_error = 3
class UseModuleError:
    # 礼包不存在
    Use_not_exist = 1
    # 礼包不够
    Use_not_enough = 2
    # 操作数据库出错
    Use_db_error = 3
class MaterialModuleError:
    # 礼包不存在
    Material_not_exist = 1
    # 礼包不够
    Material_not_enough = 2
    # 操作数据库出错
    Material_db_error = 3
class CardMgrModuleError:
    # 卡不存在
    Card_not_exist = 1
    # 不是经验丹
    Card_not_exp_use = 2
    # 数量不足
    Card_not_enough_use = 3
    # 已经最高等级
    Card_is_max_level = 4
    # 材料数量不足
    Material_not_enough = 5
    # 突破成功
    Strike_sucess = 6
    # 突破最大级
    Strike_is_max = 7
    # 碎片转换成功
    Switch_is_sucess = 8
    # 金钱不足
    Money_not_enough = 9
    # 进阶成功
    Slevel_sucess = 10
    # 球员传承不能是本人
    InHerit_is_not_self = 11
    # 球员传承不能是主角
    InHerit_is_not_main = 12
    # 传承者等级必须比被传承者大
    InHerit_level_is_enough = 13
    # 球员已达到最大级
    Baller_level_is_max = 14
    # 当前属性已满级
    Property_is_max = 15
    # 能力提升成功
    Ability_is_sucess = 16
    # 球员升级成功
    Level_is_sucess = 17
    # 球员意识提升成功
    Mentality_is_sucess = 18

class GuildModuleError:
    # 公会名字不符合规则
    Guild_name_error = 1

    # 公会简介不符合规则
    Guild_introduction_error = 2

    # 钻石不足
    Guild_diamond_not_enough = 3

    # 重复的名字
    Guild_repeat_name = 4

    # 已经加入公会
    Guild_already_in_guild = 5
    # 不存在的公会
    Guild_guild_not_exist = 6
    # 不在公会中
    Guild_not_in_guild = 7

    # 已经申请了
    Guild_already_apply = 8

    # 公会简介不符合规则
    Guild_notice_error = 9
    # 还没加入公会
    Guild_has_not_join = 10
    # 没有权利
    Guild_not_has_the_power = 11

    # 公会人员已满，请腾出空间再试！
    Guild_is_full = 12

    # 领袖离线时间不到7天
    Guild_leader_offline_not_enough = 13

    #欧元不足
    Guild_euro_not_enough = 14

    # 该职位人员已满，请腾出空间再试！
    Guild_power_is_full = 15
    # 不能超过公会等级
    Guild_level_not_enough = 16
    # 公会资金不足
    Guild_guildFunds_not_enough = 17


    # 上诉公会在保护时间
    Guild_is_by_prtected = 19

    # 该玩家取消申请
    Guild_applye_by_cancel= 26
    # 公会名字拥有非法字符
    Guild_name_has_illegality = 28
    # 公会简介拥有非法字符
    Guild_intro_has_illegality = 29

    # 公会上诉曝光道具不足
    Guild_appeal_not_enough = 30
    # 上诉曝光失败
    Guild_appeal_fail = 31
    # 拉拢失败
    Guild_rope_fail = 32
    # 拉拢次数不足
    Guild_not_rope_times= 33
    # 顾问数量已达最大
    Guild_adviser_num_error=34
    # 顾问已结被拉拢
    Guild_adviser_is_by_rope=35
    # 该顾问不属于该公会
    Guild_adviser_not_belong=36
    # 该任务已经发布
    Guild_already_exit_task=38
    # 该任务还没有完成
    Guild_task_not_finish=39
    # 公会等级不足无法发布
    Guild_level_not_enough=40
    # 顾问已经被其他公会拉拢
    Guild_adviser_already_rope=41



class BabyModuleError:
    # 宝贝不存在
    Baby_not_exist = 1
    # 时装已满级
    Clothes_level_max = 2
    # 时装已满星
    Clothes_star_max = 3
    # 欧元不足
    Money_not_enough = 4
    # 材料不足
    Material_not_enough = 5
    # 更换
    Change_is_sucess = 6
    # 时装不存在
    Clothes_not_exist = 7
    # 传承成功
    Inherit_is_sucess = 8
    # 触摸成功
    Touch_is_sucess = 9
    # 好感度已满
    Liking_is_max = 10
    # 已领取
    Have_GetReward = 11


class SkillModuleError:
    # 技能和操作不匹配
    not_match_skill = 1
    # 错误的操作
    worong_op = 2
    # 教练时间不足
    coach_time_not_enough = 3
    # 技能升级成功
    skill_up_sucess = 4
    # 技能满级
    skill_is_max = 5

class GameShopModuleError:
    # 欧元不足
    Euro_not_enough = 1
    # 钻石不足
    Diamod_not_enough = 2
    # 黑市币
    Black_not_enough = 3
    # 购买成功
    Shopping_sucess = 4
    # 公会币
    Guild_not_enough = 5



class CloneModuleError:
    # 副本未开启
    clone_not_open = 1
    # 剩余挑战次数不足
    clone_not_enough_rest_count = 2
    # 体力不足
    clone_not_enough_power = 3
    # 不足三星
    clone_not_enough_3Star = 4
    # 配置错误
    clone_config_error = 5
    # 章节未开启
    clone_chapter_not_open = 6
    # 章节奖励已领取
    clone_chapter_reward_has_got = 7
    # 章节星不够
    clone_chapter_reward_not_enough_star = 8



class ArenaModuleError:
    # 次数不足
    Buy_times_is_not_enough = 1
    # 购买成功
    Buy_times_is_Sucess = 2

class OfficialModulerror:
    # 报名成功
    signUp_sucess = 1
    # 已经报过名
    have_signUp = 2
    # 名望不足
    fame_is_not_enough = 3
    # 报名上限
    signUp_is_max = 4
    # 晋升失败
    promotion_fail = 5
    # 购买行动力成功
    buy_linePower_sucess = 6
    # 领取俸禄
    get_official_reward = 7
    # 购买行动力次数上限
    buy_linePower_fail= 8
    # 行动力不足
    linePower_is_not_enough = 9
    # 挑战成功
    fight_sucess = 10
    # 挑战失败
    fight_fail = 11
    # 废除成功
    abolition_sucess = 12
    # 废除失败
    abolition_fail = 13
    # 无法挑战
    cannot_fight_others = 14
    # 官职高
    official_cannot_up = 15
    # 次数不够
    prmissionInfo_not_times = 16
    # 有保护的
    isProtected = 17
    # 次数上线
    useTopLimit = 18



















