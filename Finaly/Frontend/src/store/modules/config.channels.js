import config from '@/api/config';

export default {
    state: {
        channels: [],
        new_channel: {
            // name: "",
            // ip: ,
            // port: "",
            // type: "",
        }
    },

    getters: {
        CHANNELS(state) {
            return state.channels;
        },
        NEW_CHANNEL(state) {
            return state.new_channel
        }
    },
    mutations: {
        SET_CHANNELS: (state, channels) => {
            state.channels = channels;
        },
        SET_NEW_CHANNEL: (state, new_channel) => {
            state.new_channel = new_channel;
        }
    },
    actions: {
        GET_CHANNELS_FROM_API({commit}) {
            config.get_channels()
                .then((channels) => {
                    commit('SET_CHANNELS', channels.data);
                    return channels;
                });
        },

        ADD_CHANNEL({commit}, new_channel) {
            config.add_channel(new_channel)
                .then((new_channel) => {
                    commit('SET_NEW_CHANNEL', new_channel.data);
                    return new_channel;
                });
        },
        SAVE_CONFIG({commit}) {
            config.save_config()
                .then((response) => {
                    // response('SET_CHANNELS', channels.data);
                    console.log(response);
                    return response;
                });
        },
        RELOAD({commit}) {
            config.reload()
                .then((response) => {
                    // response('SET_CHANNELS', channels.data);
                    console.log(response);
                    return response;
                });
        }
    },
};