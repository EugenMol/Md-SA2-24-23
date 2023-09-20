import config from '@/api/config';

export default {
    state: {
        meters: [],
        new_meter: "",
        groups: []
    },

    getters: {
        METERS(state) {
            return state.meters;
        },
        NEW_METERS(state) {
            return state.new_meter
        }
    },
    mutations: {
        // SET_GROUPS: (state, meter) => {
        //     state.groups.filter(meter);
        // },
        SET_METERS: (state, meters) => {
            state.meters = meters;
        },
        SET_NEW_METER: (state, new_meter) => {
            state.new_meter = new_meter;
            state.meters.push(new_meter)
        }
    },
    actions: {
        GET_METERS_FROM_API({commit}) {
            config.get_meters()
                .then((meters) => {
                    commit('SET_METERS', meters.data);
                    return meters;
                });

        },
        ADD_METER({commit}, new_meter) {
            console.log(new_meter)
            config.add_meter(new_meter)
                .then((response) => {
                    commit('SET_NEW_METER', response.data);
                    return response;
                });
        },
        UPDATE_METER({commit}, meter) {
            console.log(meter)
            config.update_meter(meter)
                .then((response) => {
                    commit('SET_NEW_METER', response.data);
                    return response;
                });
        },
        EXCLUDE_METER({commit}, meter) {
            config.exclude_meter(meter)
                .then((response) => {
                    commit('SET_NEW_METER', response.data);
                    // commit('SET_GROUPS', meter);
                    return response;
                });
        },
    }
}