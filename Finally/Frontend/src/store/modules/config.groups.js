import config from '@/api/config';

export default {
    state: {
        groups: [],
    },

    getters: {
        GROUPS(state) {
            return state.groups;
        },
    },
    mutations: {
        SET_GROUPS: (state, groups) => {
            state.groups = groups;
        },
        ADD_GROUP: (state, new_group) => {
            state.groups.push(new_group);
        },
        SET_METER_IN_GROUP(state, payload) {
            state.groups[payload.idx].meters.push(payload.meter)
        },
    },
    actions: {
        GET_GROUPS_FROM_API({commit}) {
            config.get_groups()
                .then((groups) => {
                    commit('SET_GROUPS', groups.data);
                    return groups;
                });

        }
        ,
        POST_ADD_GROUP({commit}, new_group) {
            config.add_group(new_group)
                .then((response) => {
                    // const group = {group_name: }
                    commit('ADD_GROUP', response.data);
                    return response;
                });
        },

        INCLUDE_METER_IN_GROUP({commit}, meter) {
            config.include_meter(meter)
                .then((response) => {
                    commit('SET_METER_IN_GROUP', meter);
                    return response;
                });
        },

        // EXCLUDE_METER({commit}, meter) {
        //     config.exclude_meter(meter)
        //         .then((response) => {
        //             commit('SET_NEW_METER', response.data);
        //             return response;
        //         });
        // },
    }
}