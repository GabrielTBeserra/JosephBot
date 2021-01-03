import json
import os.path


class Database:
    def write_in(self, guildid, obj):
        with open(f'database/{guildid}.json', 'w') as outfile:
            json.dump(obj, outfile)

    def read_out(self, guildid):
        if os.path.exists(f'database/{guildid}.json'):
            with open(f'database/{guildid}.json') as outfile:
                return json.load(outfile)
        else:
            default_guild_config = {
                'id': guildid,
                'prefix': '.'
            }
            self.write_in(guildid, default_guild_config)
            with open(f'database/{guildid}.json') as outfile:
                return json.load(outfile)

    def add_to_data(self, guildid, userid):
        data = self.read_out(id)
        new_user = {userid: {'xp': 0}}
        data[f'users'] = new_user
        self.write_in(id, data)

    def change_prefix(self, id, obj):
        data = self.read_out(id)
        data['prefix'] = obj
        self.write_in(id, data)

    '''
    Caso o usuario exista naquele servidor, retorna seu
    Caso nao exista, cria um objeto no json, e retorna 0
    '''

    def get_xp(self, id, userid):
        data = self.read_out(id)
        try:
            return data[f'users'][f'{userid}']
        except:
            new_user = {userid: {'xp': 0}}
            user = data[f'users']
            user.update(new_user)
            data[f'users'] = user
            self.write_in(id, data)
            return {'xp': 0}

    def add_xp(self, id, userid, points):
        try:
            data = self.read_out(id)
            xp = data[f'users'][f'{userid}']['xp']
            data[f'users'][f'{userid}']['xp'] = xp + points
            self.write_in(id, data)
        except:
            pass

    def enable_auto_role(self, id, isEnable: bool):
        try:
            data = self.read_out(id)
            data[f'auto_role_enable'] = isEnable
            self.write_in(id, data)
        except:
            pass

    def set_auto_role(self, id, role_id):
        try:
            data = self.read_out(id)
            data[f'auto_role'] = role_id
            self.write_in(id, data)
        except:
            pass

    def auto_role_is_enable(self, id):
        try:
            data = self.read_out(id)
            return data[f'auto_role_enable']
        except:
            pass

    def get_auto_role_id(self, id):
        try:
            data = self.read_out(id)
            return data[f'auto_role']
        except:
            pass
