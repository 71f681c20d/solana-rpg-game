# Built with Seahorse v0.2.0
#

from seahorse.prelude import *

declare_id('FtBAJhE4j9qdH8zT5VMexW3b3Abiui3QTpLNmX2CQEei');


class UserAccount(Account):
    authority: Pubkey
    score: u64
    map: u8
    health: u8


class ItemAccount(Account):
    authority: Pubkey
    id: u8
    quantity: u64
    exports: u8


@instruction
def init_user(authority: Signer, new_user_account: Empty[UserAccount]):
    user_account = new_user_account.init(
        payer=authority, seeds=['user', authority])
    user_account.authority = authority.key()
    user_account.score = 0
    user_account.map = 0
    user_account.health = 0

@instruction
def init_item(authority: Signer, new_item_account: Empty[ItemAccount], id: u8):
    item_account = new_item_account.init(
        payer=authority, seeds=['item', authority, id])
    item_account.authority = authority.key()
    item_account.id = id
    item_account.quantity = 0
    item_account.exports = 0

@instruction
def set_user(authority: Signer, user_account: UserAccount, score: u64, map: u8, health: u8):
    assert authority.key() == user_account.authority, "signer must be user account authority"
    user_account.score = score
    user_account.map = map
    user_account.health = health

@instruction
def add_item(authority: Signer, item_account: ItemAccount):
    assert authority.key() == item_account.authority, "signer must be user account authority"
    item_account.quantity = item_account.quantity + 1

@instruction
def export_items(authority: Signer, item_account: ItemAccount):
    assert authority.key() == item_account.authority, "signer must be user account authority"
    item_account.quantity = 0
    item_account.exports = item_account.exports + 1

