<template>

    <div v-if="!loaded" id="loadScreen">
        <div class="row row-cols-1 g-2 justify-content-center">
            <div class="col text-center"><h1 class="text-light">NG 太空公司</h1></div>
            <div class="col text-center"><img id="loadLogo" style="width:25%; height:auto;" src="https://ngspacecompany.exileng.com/whiteLogo.png" alt="Game logo" /></div>
            <div class="col text-center"><h5 class="text-light">网状样条...</h5></div>
        </div>
    </div>

    <div v-if="loaded" id="gameScreen">
        <div id="sidebar" :class="{ 'open':sidebarOpen }" role="navigation">
            <top-header class="px-2">
                <div class="col-auto">
                    <img src="https://ngspacecompany.exileng.com/whiteLogo.png" width="42" height="42" alt="Game logo" />
                </div>

                <div class="col text-truncate px-0">
                    <span class="h5 text-light mb-0">{{ companyName }} Company</span>
                </div>

                <div class="col-auto px-0">
                    <button class="btn p-1" @click="changeLogModal.show();">
                        <small class="small text-normal">v{{ currentRelease }}</small>
                    </button>
                </div>

                <div class="col-auto d-lg-none">
                    <button @click="sidebarOpen = false;">
                        <i class="fas fa-fw fa-times"></i>
                    </button>
                </div>

            </top-header>
            <inner-content data-simplebar class="pe-2">
                <div class="row gx-2 gy-3 row-cols-1">

                    <sidenav-item v-if="showRoadmap" id="helpPane" icon="help.png" unlocked="true" />

                    <sidenav-group id="pinnedHeading" :unlocked="displayPinnedItems == true">
                        <sidenav-item v-for="pane in pinned" :key="pane.id" :id="pane.id" :icon="pane.icon" unlocked="true" :prod="data[pane.resId].prod" :count="data[pane.resId].count" :storage="getStorageCap(pane.resId)" :cap="data[pane.resId].storage" :problem="data[pane.resId].problem" :buildingStorageId="pane.buildingStorageId" />
                    </sidenav-group>

                    <sidenav-group id="energyHeading" :unlocked="data['energy'].unlocked">
                        <sidenav-item id="energyPane" icon="energy.png" :unlocked="data['energy'].unlocked" :prod="data['energy'].prod" :problem="data['energy'].problem" />
                        <sidenav-item id="batteryPane" icon="battery.png" :unlocked="data['energy'].unlocked" :count="data['energy'].count" :storage="getStorageCap('energy')" :cap="data['energy'].storage" />
                    </sidenav-group>

                    <sidenav-group id="fabricatedHeading" :unlocked="data['carbon'].unlocked">
                        <sidenav-item id="plasmaPane" icon="plasma.png" :unlocked="data['plasma'].unlocked" :prod="data['plasma'].prod" :count="data['plasma'].count" :storage="getStorageCap('plasma')" :cap="data['plasma'].storage" :problem="data['plasma'].problem" />
                        <sidenav-item id="meteoritePane" icon="meteorite.png" :unlocked="data['meteorite'].unlocked" :prod="data['meteorite'].prod" :count="data['meteorite'].count" :storage="getStorageCap('meteorite')" :cap="data['meteorite'].storage" :problem="data['meteorite'].problem" buildingStorageId="meteoriteS1" />
                        <sidenav-item id="carbonPane" icon="carbon.png" :unlocked="data['carbon'].unlocked" :prod="data['carbon'].prod" :count="data['carbon'].count" :storage="getStorageCap('carbon')" :cap="data['carbon'].storage" :problem="data['carbon'].problem" buildingStorageId="carbonS1" />
                    </sidenav-group>

                    <sidenav-group id="earthResourcesHeading" :unlocked="data['metal'].unlocked">
                        <sidenav-item id="oilPane" icon="oil.png" :unlocked="data['oil'].unlocked" :prod="data['oil'].prod" :count="data['oil'].count" :storage="getStorageCap('oil')" :cap="data['oil'].storage" buildingStorageId="oilS1" />
                        <sidenav-item id="metalPane" icon="metal.png" :unlocked="data['metal'].unlocked" :prod="data['metal'].prod" :count="data['metal'].count" :storage="getStorageCap('metal')" :cap="data['metal'].storage" buildingStorageId="metalS1" />
                        <sidenav-item id="gemPane" icon="gem.png" :unlocked="data['gem'].unlocked" :prod="data['gem'].prod" :count="data['gem'].count" :storage="getStorageCap('gem')" :cap="data['gem'].storage" buildingStorageId="gemS1" />
                        <sidenav-item id="woodPane" icon="wood.png" :unlocked="data['wood'].unlocked" :prod="data['wood'].prod" :count="data['wood'].count" :storage="getStorageCap('wood')" :cap="data['wood'].storage" buildingStorageId="woodS1" />
                        <sidenav-item id="siliconPane" icon="silicon.png" :unlocked="data['silicon'].unlocked" :prod="data['silicon'].prod" :count="data['silicon'].count" :storage="getStorageCap('silicon')" :cap="data['silicon'].storage" buildingStorageId="siliconS1" />
                        <sidenav-item id="uraniumPane" icon="uranium.png" :unlocked="data['uranium'].unlocked" :prod="data['uranium'].prod" :count="data['uranium'].count" :storage="getStorageCap('uranium')" :cap="data['uranium'].storage" buildingStorageId="uraniumS1" />
                        <sidenav-item id="lavaPane" icon="lava.png" :unlocked="data['lava'].unlocked" :prod="data['lava'].prod" :count="data['lava'].count" :storage="getStorageCap('lava')" :cap="data['lava'].storage" buildingStorageId="lavaS1" />
                    </sidenav-group>

                    <sidenav-group id="innerResourcesHeading" :unlocked="data['lunarite'].unlocked">
                        <sidenav-item id="lunaritePane" icon="lunarite.png" :unlocked="data['lunarite'].unlocked" :prod="data['lunarite'].prod" :count="data['lunarite'].count" :storage="getStorageCap('lunarite')" :cap="data['lunarite'].storage" buildingStorageId="lunariteS1" />
                        <sidenav-item id="methanePane" icon="methane.png" :unlocked="data['methane'].unlocked" :prod="data['methane'].prod" :count="data['methane'].count" :storage="getStorageCap('methane')" :cap="data['methane'].storage" buildingStorageId="methaneS1" />
                        <sidenav-item id="titaniumPane" icon="titanium.png" :unlocked="data['titanium'].unlocked" :prod="data['titanium'].prod" :count="data['titanium'].count" :storage="getStorageCap('titanium')" :cap="data['titanium'].storage" buildingStorageId="titaniumS1" />
                        <sidenav-item id="goldPane" icon="gold.png" :unlocked="data['gold'].unlocked" :prod="data['gold'].prod" :count="data['gold'].count" :storage="getStorageCap('gold')" :cap="data['gold'].storage" buildingStorageId="goldS1" />
                        <sidenav-item id="silverPane" icon="silver.png" :unlocked="data['silver'].unlocked" :prod="data['silver'].prod" :count="data['silver'].count" :storage="getStorageCap('silver')" :cap="data['silver'].storage" buildingStorageId="silverS1" />
                    </sidenav-group>

                    <sidenav-group id="outerResourcesHeading" :unlocked="data['hydrogen'].unlocked || data['helium'].unlocked || data['ice'].unlocked">
                        <sidenav-item id="hydrogenPane" icon="hydrogen.png" :unlocked="data['hydrogen'].unlocked" :prod="data['hydrogen'].prod" :count="data['hydrogen'].count" :storage="getStorageCap('hydrogen')" :cap="data['hydrogen'].storage" buildingStorageId="hydrogenS1" />
                        <sidenav-item id="heliumPane" icon="helium.png" :unlocked="data['helium'].unlocked" :prod="data['helium'].prod" :count="data['helium'].count" :storage="getStorageCap('helium')" :cap="data['helium'].storage" buildingStorageId="heliumS1" />
                        <sidenav-item id="icePane" icon="ice.png" :unlocked="data['ice'].unlocked" :prod="data['ice'].prod" :count="data['ice'].count" :storage="getStorageCap('ice')" :cap="data['ice'].storage" buildingStorageId="iceS1" />
                    </sidenav-group>

                    <sidenav-group id="researchesHeading" :unlocked="data['science'].unlocked">
                        <sidenav-item id="sciencePane" icon="science.png" :unlocked="data['science'].unlocked" :prod="data['science'].prod" :count="data['science'].count" />
                        <sidenav-item id="technologiesPane" icon="technologies.png" :unlocked="data['science'].unlocked" />
                    </sidenav-group>

                    <sidenav-group id="solSytemHeading" :unlocked="data['fuel'].unlocked">
                        <sidenav-item id="fuelPane" icon="fuel.png" :unlocked="data['fuel'].unlocked" :prod="data['fuel'].prod" :count="data['fuel'].count" />
                        <sidenav-item id="rocketPane" icon="rocket.png" :unlocked="data['rocket1'].unlocked" :done="data['rocket2'].count > 0" doneText="launched" />
                        <sidenav-item id="innerSolarSystemPane" icon="innerSolarSystem.png" :unlocked="data['moon'].unlocked" :done="data['wonderStation'].count > 0" doneText="explored" />
                        <sidenav-item id="outerSolarSystemPane" icon="outerSolarSystem.png" :unlocked="data['jupiter'].unlocked" :done="data['solCenter1'].count > 0" doneText="explored" />
                    </sidenav-group>

                    <sidenav-group id="wondersHeading" :unlocked="data['wonderPrecious0'].unlocked">
                        <sidenav-item id="wonderStationPane" icon="wonderStation.png" :unlocked="data['wonderPrecious0'].unlocked" :done="data['wonderPrecious0'].count > 0 && data['wonderEnergetic0'].count > 0 && data['wonderTechnological0'].count > 0 && data['wonderMeteorite0'].count > 0" doneText="done" />
                        <sidenav-item id="floor1Pane" icon="floor1.png" :unlocked="data['wonderPrecious1'].unlocked || data['wonderEnergetic1'].unlocked || data['wonderTechnological1'].unlocked || data['wonderMeteorite1'].unlocked" :done="data['wonderPrecious1'].count > 0 && data['wonderEnergetic1'].count > 0 && data['wonderTechnological1'].count > 0 && data['wonderMeteorite1'].count > 0" doneText="done" />
                        <sidenav-item id="floor2Pane" icon="floor2.png" :unlocked="data['wonderComm'].unlocked" :done="data['wonderComm'].count > 0 && data['wonderSpaceship'].count > 0 && data['wonderAntimatter'].count > 0 && data['wonderPortal'].count > 0" doneText="done" />
                        <sidenav-item id="floor3Pane" icon="floor3.png" :unlocked="data['wonderStargate'].unlocked" :done="data['wonderStargate'].count > 0" doneText="done" />
                    </sidenav-group>

                    <sidenav-group id="solCenterHeading" :unlocked="data['techPlasma0'].unlocked">
                        <sidenav-item id="solCenterPane" icon="solCenter.png" :unlocked="data['techPlasma0'].unlocked" :done="data['techPlasma0'].count > 0 && data['techEmc0'].count > 0 && data['techDyson0'].count > 0" doneText="done" />
                        <sidenav-item id="emcPane" icon="emc.png" :unlocked="data['emc'].unlocked" />
                        <sidenav-item id="dysonPane" icon="dyson.png" :unlocked="data['segment'].unlocked" />
                        <sidenav-item id="nanoswarmPane" icon="nanoswarm.png" :unlocked="data['nanoswarm'].unlocked" />
                    </sidenav-group>

                    <sidenav-group id="interstellarHeading" :unlocked="data['radarT1'].unlocked || data['antimatter'].unlocked || data['spaceship'].unlocked || data['shipT1'].unlocked">
                        <sidenav-item id="antimatterPane" icon="antimatter.png" :unlocked="data['antimatter'].unlocked" :prod="data['antimatter'].prod" :count="data['antimatter'].count" :storage="getStorageCap('antimatter')" :cap="data['antimatter'].storage" />
                        <sidenav-item id="communicationPane" icon="communication.png" :unlocked="data['radarT1'].unlocked" />
                        <sidenav-item id="spaceshipPane" icon="spaceship.png" :unlocked="data['spaceship'].unlocked" :done="data['spaceship'].count > 0" doneText="built" />
                        <sidenav-item id="militaryPane" icon="military.png" :unlocked="data['shipT1'].unlocked" />
                        <sidenav-item id="terraformingPane" icon="terraforming.png" :unlocked="data['probe'].unlocked" />
                        <sidenav-item id="interstellarCarnelianPane" icon="carnelian.png" :unlocked="data['spaceship'].count > 0" :opinion="data['carnelian'].opinion" />
                        <sidenav-item id="interstellarPrasnianPane" icon="prasnian.png" :unlocked="data['spaceship'].count > 0" :opinion="data['prasnian'].opinion" />
                        <sidenav-item id="interstellarHyacinitePane" icon="hyacinite.png" :unlocked="data['spaceship'].count > 0" :opinion="data['hyacinite'].opinion" />
                        <sidenav-item id="interstellarKitrinosPane" icon="kitrinos.png" :unlocked="data['spaceship'].count > 0" :opinion="data['kitrinos'].opinion" />
                        <sidenav-item id="interstellarMovitonPane" icon="moviton.png" :unlocked="data['spaceship'].count > 0" :opinion="data['moviton'].opinion" />
                        <sidenav-item id="interstellarOverlordPane" icon="overlord.png" :unlocked="data['overlordProgram'].count > 0" />
                    </sidenav-group>

                    <sidenav-group id="stargazeHeading" :unlocked="data['darkmatter'].unlocked">
                        <sidenav-item id="darkmatterPane" icon="darkmatter.png" :unlocked="data['darkmatter'].unlocked" :count="darkmatter" :potential="getPotentialDM" />
                        <sidenav-item id="stargazeCarnelianPane" icon="carnelian.png" :unlocked="data['darkmatter'].unlocked" :opinion="data['carnelian'].opinion" />
                        <sidenav-item id="stargazePrasnianPane" icon="prasnian.png" :unlocked="data['darkmatter'].unlocked" :opinion="data['prasnian'].opinion" />
                        <sidenav-item id="stargazeHyacinitePane" icon="hyacinite.png" :unlocked="data['darkmatter'].unlocked" :opinion="data['hyacinite'].opinion" />
                        <sidenav-item id="stargazeKitrinosPane" icon="kitrinos.png" :unlocked="data['darkmatter'].unlocked" :opinion="data['kitrinos'].opinion" />
                        <sidenav-item id="stargazeMovitonPane" icon="moviton.png" :unlocked="data['darkmatter'].unlocked" :opinion="data['moviton'].opinion" />
                        <sidenav-item id="stargazeOverlordPane" icon="overlord.png" :unlocked="data['darkmatter'].unlocked" :opinion="data['overlord'].opinion" />
                    </sidenav-group>

                    <sidenav-group id="enlightenmentHeading" :unlocked="data['ultrite'].unlocked">
                        <sidenav-item id="ultritePane" icon="ultrite.png" :unlocked="data['ultrite'].unlocked" :count="ultrite" :potential="getPotentialUL" />
                        <sidenav-item id="titansPane" icon="titans.png" :unlocked="data['ultrite'].unlocked" />
                        <sidenav-item id="upgradesPane" icon="upgrades.png" :unlocked="data['ultrite'].unlocked" />
                    </sidenav-group>
                </div>
            </inner-content>
        </div>
        <div id="page">
            <top-header>

                <div class="col-auto d-lg-none position-relative">
                    <button @click="sidebarOpen = true;">
                        <div v-if="hasNotif" class="position-absolute top-0 end-0" style="line-height:1">
                            <i class="fas fa-fw fa-certificate text-success small"></i>
                        </div>
                        <img :src="require('./assets/whiteLogo.png')" width="36" height="36" alt="Game logo" />
                    </button>
                </div>

                <div class="col-auto ms-auto">
                    <a href="https://discord.gg/3UkgeeT9CV" target="_blank" data-bs-toggle="tooltip" data-bs-placement="left" title="Discord">
                        <img :src="require('./assets/interface/discord.png')" width="16" height="16" alt="Discord icon" />
                    </a>
                </div>

                <div class="col-auto cursor-hover">
                    <button @click="setActivePane('donatingPane')">
                        <img :src="require('./assets/interface/donating.png')" width="16" height="16" alt="Donating icon" />
                        <span class="ms-1 text-light">{{ $t('donatingPane') }}</span>
                    </button>
                </div>

                <div class="col-auto cursor-hover position-relative" data-bs-toggle="tooltip" data-bs-placement="left" :title="$t('achievementPane')">
                    <button @click="setActivePane('achievementPane')">
                        <div v-if="isNotif('achievementPane')" class="position-absolute top-0 end-0" style="line-height:1">
                            <i class="fas fa-fw fa-certificate text-success small"></i>
                        </div>
                        <img :src="require('./assets/interface/trophy.png')" width="16" height="16" alt="Achievements icon" />
                    </button>
                </div>

                <div class="col-auto cursor-hover position-relative" data-bs-toggle="tooltip" data-bs-placement="left" :title="$t('rankPane')">
                    <button @click="setActivePane('rankPane')">
                        <img :src="require('./assets/interface/rank.png')" width="16" height="16" alt="Leaderboard icon" />
                    </button>
                </div>

                <div class="col-auto">
                    <button id="dropdownLanguageButton" class="text-normal cursor-hover" data-bs-toggle="dropdown" aria-expanded="false" aria-label="Language dropdown">
                      <span v-if="locale == 'chs'" class="flag-icon flag-icon-cn rounded"></span>
                        <span v-if="locale == 'en'" class="flag-icon flag-icon-gb rounded"></span>
                        <span v-if="locale == 'fr'" class="flag-icon flag-icon-fr rounded"></span>
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownLanguageButton">
                      <li>
                        <button class="dropdown-item cursor-hover" @click="changeLocale('chs')">
                          <span class="flag-icon flag-icon-cn rounded me-2"></span>
                          中文
                        </button>
                      </li>
                        <li>
                            <button class="dropdown-item cursor-hover" @click="changeLocale('en')">
                                <span class="flag-icon flag-icon-gb rounded me-2"></span>
                                English
                            </button>
                        </li>
                        <li>
                            <button class="dropdown-item cursor-hover" @click="changeLocale('fr')">
                                <span class="flag-icon flag-icon-fr rounded me-2"></span>
                                Français
                            </button>
                        </li>
                    </ul>
                </div>

                <div class="col-auto">
                    <button id="dropdownMenuButton" class="text-light cursor-hover" data-bs-toggle="dropdown" aria-expanded="false" aria-label="Menu dropdown">
                        <i class="fas fa-fw fa-ellipsis-v"></i>
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton">
                        <li>
                            <button class="dropdown-item cursor-hover" @click="setActivePane('settingsPane')">
                                <img :src="require('./assets/interface/cog.png')" width="16" height="16" class="me-2" alt="Settings icon" />
                                {{ $t('settingsPane') }}
                            </button>
                        </li>
                        <li>
                            <button class="dropdown-item cursor-hover" @click="setActivePane('aboutPane')">
                                <img :src="require('./assets/interface/about.png')" width="16" height="16" class="me-2" alt="About icon" />
                                {{ $t('aboutPane') }}
                            </button>
                        </li>
                    </ul>
                </div>

            </top-header>
            <inner-content data-simplebar role="main">

                <div v-if="ghLatestRelease && ghLatestRelease != currentRelease" class="alert alert-warning text-end" role="alert">
                    <small>{{ $t('ghLatestVersion') }}</small>
                    <small class="mx-2">v{{ ghLatestRelease }}</small>
                    <button class="btn" @click="onRefresh()">{{ $t('update') }}</button>
                </div>

                <div class="tab-content" style="padding-bottom: 65px;">

                    <!-- ENERGY PANE -->
                    <pane id="energyPane" icon="energy.png" :descs="['energyPane_desc']" pinnable="energy">
                        <resource id="energy" />
                        <buildable id="energyT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="energyT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techEnergy2" />
                        <buildable id="energyT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="venus" />
                        <buildable id="energyT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderPrecious1" />
                        <buildable id="energyT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderEnergetic1" />
                        <buildable id="energyT6" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="jupiter" />
                    </pane>

                    <!-- BATTERY PANE -->
                    <pane id="batteryPane" icon="battery.png" :descs="['batteryPane_desc']">
                        <buildable id="energyS1" btnText="build" collapse="true" unlocker="techEnergyStorage1" />
                        <buildable id="energyS2" btnText="build" collapse="true" unlocker="techEnergyStorage2" />
                        <buildable id="energyS3" btnText="build" collapse="true" unlocker="techEnergyStorage3" />
                        <buildable id="energyS4" btnText="build" collapse="true" unlocker="techEnergyStorage4" />
                        <buildable id="energyS5" btnText="build" collapse="true" unlocker="techEnergyStorage5" />
                        <buildable id="energyS6" btnText="build" collapse="true" unlocker="techEnergyStorage6" />
                    </pane>

                    <!-- PLASMA PANE -->
                    <pane id="plasmaPane" icon="plasma.png" :descs="['plasmaPane_desc']" pinnable="plasma">
                        <resource id="plasma" />
                        <buildable id="plasmaT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techPlasma1" />
                        <buildable id="plasmaT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techPlasma2" />
                        <buildable id="plasmaT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techPlasma3" />
                        <buildable id="plasmaT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techPlasma4" />
                        <buildable id="plasmaS1" btnText="build" collapse="true" unlocker="techPlasmaStorage1" />
                        <buildable id="plasmaS2" btnText="build" collapse="true" unlocker="techPlasmaStorage2" />
                        <buildable id="plasmaS3" btnText="build" collapse="true" unlocker="techPlasmaStorage3" />
                        <buildable id="plasmaS4" btnText="build" collapse="true" unlocker="techPlasmaStorage4" />
                    </pane>

                    <!-- METEORITE PANE -->
                    <pane id="meteoritePane" icon="meteorite.png" :descs="['meteoritePane_desc']" pinnable="meteorite" shortcutBuildingStorageId="meteoriteS1">
                        <resource id="meteorite" />
                        <buildable id="meteoriteS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="meteoriteT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techMeteorite1" />
                        <buildable id="meteoriteT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techMeteorite2" />
                        <buildable id="meteoriteT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techMeteorite3" />
                        <buildable id="meteoriteT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techMeteorite4" />
                    </pane>

                    <!-- CARBON PANE -->
                    <pane id="carbonPane" icon="carbon.png" :descs="['carbonPane_desc']" pinnable="carbon" shortcutBuildingStorageId="carbonS1">
                        <resource id="carbon" />
                        <buildable id="carbonS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="carbonT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="carbonT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="carbonT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="carbonT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="carbonT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- OIL PANE -->
                    <pane id="oilPane" icon="oil.png" :descs="['oilPane_desc']" pinnable="oil" shortcutBuildingStorageId="oilS1">
                        <resource id="oil" />
                        <buildable id="oilS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="oilT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="oilT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="oilT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="oilT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="oilT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- METAL PANE -->
                    <pane id="metalPane" icon="metal.png" :descs="['metalPane_desc']" pinnable="metal" shortcutBuildingStorageId="metalS1">
                        <resource id="metal" />
                        <buildable id="metalS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="metalT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="metalT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="metalT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="metalT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="metalT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- GEM PANE -->
                    <pane id="gemPane" icon="gem.png" :descs="['gemPane_desc']" pinnable="gem" shortcutBuildingStorageId="gemS1">
                        <resource id="gem" />
                        <buildable id="gemS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="gemT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="gemT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="gemT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="gemT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="gemT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- WOOD PANE -->
                    <pane id="woodPane" icon="wood.png" :descs="['woodPane_desc']" pinnable="wood" shortcutBuildingStorageId="woodS1">
                        <resource id="wood" />
                        <buildable id="woodS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="woodT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="woodT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="woodT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="woodT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="woodT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- SILICON PANE -->
                    <pane id="siliconPane" icon="silicon.png" :descs="['siliconPane_desc']" pinnable="silicon" shortcutBuildingStorageId="siliconS1">
                        <resource id="silicon" />
                        <buildable id="siliconS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="siliconT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="siliconT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="siliconT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="siliconT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="siliconT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- URANIUM PANE -->
                    <pane id="uraniumPane" icon="uranium.png" :descs="['uraniumPane_desc']" pinnable="uranium" shortcutBuildingStorageId="uraniumS1">
                        <resource id="uranium" />
                        <buildable id="uraniumS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="uraniumT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="uraniumT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="uraniumT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="uraniumT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="uraniumT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- LAVA PANE -->
                    <pane id="lavaPane" icon="lava.png" :descs="['lavaPane_desc']" pinnable="lava" shortcutBuildingStorageId="lavaS1">
                        <resource id="lava" />
                        <buildable id="lavaS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="lavaT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="lavaT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="lavaT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="lavaT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="lavaT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- LUNARITE PANE -->
                    <pane id="lunaritePane" icon="lunarite.png" :descs="['lunaritePane_desc']" pinnable="lunarite" shortcutBuildingStorageId="lunariteS1">
                        <resource id="lunarite" />
                        <buildable id="lunariteS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="lunariteT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="lunariteT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="lunariteT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="lunariteT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="lunariteT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- METHANE PANE -->
                    <pane id="methanePane" icon="methane.png" :descs="['methanePane_desc']" pinnable="methane" shortcutBuildingStorageId="methaneS1">
                        <resource id="methane" />
                        <buildable id="methaneS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="methaneT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="methaneT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="methaneT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="methaneT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="methaneT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- TITANIUM PANE -->
                    <pane id="titaniumPane" icon="titanium.png" :descs="['titaniumPane_desc']" pinnable="titanium" shortcutBuildingStorageId="titaniumS1">
                        <resource id="titanium" />
                        <buildable id="titaniumS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="titaniumT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="titaniumT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="titaniumT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="titaniumT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="titaniumT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- GOLD PANE -->
                    <pane id="goldPane" icon="gold.png" :descs="['goldPane_desc']" pinnable="gold" shortcutBuildingStorageId="goldS1">
                        <resource id="gold" />
                        <buildable id="goldS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="goldT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="goldT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="goldT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="goldT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="goldT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- SILVER PANE -->
                    <pane id="silverPane" icon="silver.png" :descs="['silverPane_desc']" pinnable="silver" shortcutBuildingStorageId="silverS1">
                        <resource id="silver" />
                        <buildable id="silverS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="silverT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="silverT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="silverT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="silverT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="silverT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- HYDROGEN PANE -->
                    <pane id="hydrogenPane" icon="hydrogen.png" :descs="['hydrogenPane_desc']" pinnable="hydrogen" shortcutBuildingStorageId="hydrogenS1">
                        <resource id="hydrogen" />
                        <buildable id="hydrogenS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="hydrogenT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="hydrogenT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="hydrogenT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="hydrogenT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="hydrogenT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- HELIUM PANE -->
                    <pane id="heliumPane" icon="helium.png" :descs="['heliumPane_desc']" pinnable="helium" shortcutBuildingStorageId="heliumS1">
                        <resource id="helium" />
                        <buildable id="heliumS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="heliumT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="heliumT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="heliumT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="heliumT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="heliumT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- ICE PANE -->
                    <pane id="icePane" icon="ice.png" :descs="['icePane_desc']" pinnable="ice" shortcutBuildingStorageId="iceS1">
                        <resource id="ice" />
                        <buildable id="iceS1" btnText="upgrade" collapse="true" unlocker="techStorage" autoUpgradeStorage="true" />
                        <buildable id="iceT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="iceT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier2" />
                        <buildable id="iceT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderTechnological1" />
                        <buildable id="iceT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="wonderMeteorite1" />
                        <buildable id="iceT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techTier5" />
                    </pane>

                    <!-- SCIENCE PANE -->
                    <pane id="sciencePane" icon="science.png" :descs="['sciencePane_desc']" pinnable="science">
                        <buildable id="scienceT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="scienceT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techScience2" />
                        <buildable id="scienceT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techScience3" />
                        <buildable id="scienceT4" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techScience4" />
                        <buildable id="scienceT5" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techScience5" />
                    </pane>

                    <!-- TECHNOLOGIES PANE -->
                    <pane id="technologiesPane" icon="technologies.png" :descs="['technologiesPane_desc']">
                        <buildable v-if="!(showDoneTechs == false && data['techStorage'].count > 0)" id="techStorage" btnText="unlock" />
                        <buildable v-if="!(showDoneTechs == false && data['techEnergy1'].count > 0)" id="techEnergy1" btnText="unlock" />
                        <buildable v-if="!(showDoneTechs == false && data['techOil'].count > 0)" id="techOil" btnText="unlock" unlocker="techStorage" />
                        <buildable v-if="!(showDoneTechs == false && data['techEnergy2'].count > 0)" id="techEnergy2" btnText="unlock" unlocker="techEnergy1" />
                        <buildable v-if="!(showDoneTechs == false && data['techTier2'].count > 0)" id="techTier2" btnText="unlock" unlocker="techEnergy1" />
                        <buildable v-if="!(showDoneTechs == false && data['techDestruction'].count > 0)" id="techDestruction" btnText="unlock" unlocker="techTier2" />
                        <buildable v-if="!(showDoneTechs == false && data['techFuel1'].count > 0)" id="techFuel1" btnText="unlock" unlocker="techTier2" />
                        <buildable v-if="!(showDoneTechs == false && data['techFuel2'].count > 0)" id="techFuel2" btnText="unlock" unlocker="techFuel1" />
                        <buildable v-if="!(showDoneTechs == false && data['techFuel3'].count > 0)" id="techFuel3" btnText="unlock" unlocker="techFuel2" />
                        <buildable v-if="!(showDoneTechs == false && data['techScience2'].count > 0)" id="techScience2" btnText="unlock" unlocker="techFuel1" />
                        <buildable v-if="!(showDoneTechs == false && data['techScience3'].count > 0)" id="techScience3" btnText="unlock" unlocker="techScience2" />
                        <buildable v-if="!(showDoneTechs == false && data['techScience4'].count > 0)" id="techScience4" btnText="unlock" unlocker="techScience3" />
                        <buildable v-if="!(showDoneTechs == false && data['techEnergyStorage1'].count > 0)" id="techEnergyStorage1" btnText="unlock" unlocker="upgradeEnergy2" />
                        <buildable v-if="!(showDoneTechs == false && data['techEnergyStorage2'].count > 0)" id="techEnergyStorage2" btnText="unlock" unlocker="techEnergyStorage1" />
                        <buildable v-if="!(showDoneTechs == false && data['techEnergyStorage3'].count > 0)" id="techEnergyStorage3" btnText="unlock" unlocker="techEnergyStorage2" />
                        <buildable v-if="!(showDoneTechs == false && data['techEnergyStorage4'].count > 0)" id="techEnergyStorage4" btnText="unlock" unlocker="techEnergyStorage4" />
                        <buildable v-if="!(showDoneTechs == false && data['techPlasma1'].count > 0)" id="techPlasma1" btnText="unlock" unlocker="techPlasma0" />
                        <buildable v-if="!(showDoneTechs == false && data['techPlasma2'].count > 0)" id="techPlasma2" btnText="unlock" unlocker="techPlasma1" />
                        <buildable v-if="!(showDoneTechs == false && data['techPlasmaStorage1'].count > 0)" id="techPlasmaStorage1" btnText="unlock" unlocker="techPlasma1" />
                        <buildable v-if="!(showDoneTechs == false && data['techPlasmaStorage2'].count > 0)" id="techPlasmaStorage2" btnText="unlock" unlocker="techPlasmaStorage1" />
                        <buildable v-if="!(showDoneTechs == false && data['techEmc1'].count > 0)" id="techEmc1" btnText="unlock" unlocker="techEmc0" />
                        <buildable v-if="!(showDoneTechs == false && data['techMeteorite0'].count > 0)" id="techMeteorite0" btnText="unlock" unlocker="techEmc1" />
                        <buildable v-if="!(showDoneTechs == false && data['techMeteorite1'].count > 0)" id="techMeteorite1" btnText="unlock" unlocker="wonderMeteorite1" />
                        <buildable v-if="!(showDoneTechs == false && data['techMeteorite2'].count > 0)" id="techMeteorite2" btnText="unlock" unlocker="techMeteorite1" />
                        <buildable v-if="!(showDoneTechs == false && data['techDyson1'].count > 0)" id="techDyson1" btnText="unlock" unlocker="techDyson0" />
                        <buildable v-if="!(showDoneTechs == false && data['techDyson2'].count > 0)" id="techDyson2" btnText="unlock" unlocker="techDyson1" />
                        <buildable v-if="!(showDoneTechs == false && data['techNanoswarm1'].count > 0)" id="techNanoswarm1" btnText="unlock" unlocker="techNanoswarm0" />
                        <buildable v-if="!(showDoneTechs == false && data['upgradeTier2'].count > 0)" id="upgradeTier2" btnText="upgrade" unlocker="techTier2" />
                        <buildable v-if="!(showDoneTechs == false && data['upgradeEnergy1'].count > 0)" id="upgradeEnergy1" btnText="upgrade" unlocker="techEnergy1" />
                        <buildable v-if="!(showDoneTechs == false && data['upgradeEnergy2'].count > 0)" id="upgradeEnergy2" btnText="upgrade" unlocker="techEnergy2" />
                        <buildable id="boostProduction" btnText="boost" />
                        <buildable id="boostScience" btnText="boost" />
                        <buildable id="boostEnergy" btnText="boost" />
                        <buildable id="boostEnergyStorage" btnText="boost" />
                    </pane>

                    <!-- FUEL PANE -->
                    <pane id="fuelPane" icon="fuel.png" :descs="['fuelPane_desc']" pinnable="fuel">
                        <resource id="fuel" />
                        <buildable id="fuelT1" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" />
                        <buildable id="fuelT2" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techFuel2" />
                        <buildable id="fuelT3" btnText="build" collapse="true" :multibuy="data['multiBuy'].count > 0" calc="true" unlocker="techFuel3" />
                    </pane>

                    <!-- ROCKET PANE -->
                    <pane id="rocketPane" icon="rocket.png" :descs="['rocketPane_desc']">
                        <buildable id="rocket1" btnText="build" />
                        <buildable id="rocket2" btnText="launch" unlocker="rocket1" />
                    </pane>

                    <!-- INNER SOLAR SYSTEM PANE -->
                    <pane id="innerSolarSystemPane" icon="innerSolarSystem.png">
                        <buildable id="moon" btnText="explore" />
                        <buildable id="mercury" btnText="explore" />
                        <buildable id="venus" btnText="explore" />
                        <buildable id="mars" btnText="explore" />
                        <buildable id="asteroid" btnText="explore" />
                        <buildable id="wonderStation" btnText="explore" unlocker="asteroid" />
                    </pane>

                    <!-- OUTER SOLAR SYSTEM PANE -->
                    <pane id="outerSolarSystemPane" icon="outerSolarSystem.png">
                        <buildable id="jupiter" btnText="explore" />
                        <buildable id="saturn" btnText="explore" />
                        <buildable id="uranus" btnText="explore" />
                        <buildable id="neptune" btnText="explore" />
                        <buildable id="pluto" btnText="explore" />
                        <buildable id="solCenter0" btnText="explore" unlocker="pluto" />
                        <buildable id="solCenter1" btnText="explore" unlocker="solCenter0" />
                    </pane>

                    <!-- WONDER STATION PANE -->
                    <pane id="wonderStationPane" icon="wonderStation.png" :descs="['wonderStationPane_desc']">
                        <buildable id="wonderPrecious0" btnText="build" />
                        <buildable id="wonderEnergetic0" btnText="build" />
                        <buildable id="wonderTechnological0" btnText="build" />
                        <buildable id="wonderMeteorite0" btnText="build" />
                    </pane>

                    <!-- FLOOR #1 PANE -->
                    <pane id="floor1Pane" icon="floor1.png">
                        <buildable id="wonderPrecious1" btnText="activate" />
                        <buildable id="wonderEnergetic1" btnText="activate" />
                        <buildable id="wonderTechnological1" btnText="activate" />
                        <buildable id="wonderMeteorite1" btnText="activate" />
                    </pane>

                    <!-- FLOOR #2 PANE -->
                    <pane id="floor2Pane" icon="floor2.png">
                        <buildable id="wonderComm" btnText="activate" />
                        <buildable id="wonderSpaceship" btnText="activate" />
                        <buildable id="wonderAntimatter" btnText="activate" />
                        <buildable id="wonderPortal" btnText="activate" />
                    </pane>

                    <!-- FLOOR #3 PANE -->
                    <pane id="floor3Pane" icon="floor3.png">
                        <buildable id="wonderStargate" btnText="activate" />
                    </pane>

                    <!-- SOL CENTER PANE -->
                    <pane id="solCenterPane" icon="solCenter.png">
                        <buildable id="techPlasma0" btnText="unlock" />
                        <buildable id="techEmc0" btnText="unlock" />
                        <buildable id="techDyson0" btnText="unlock" />
                    </pane>

                    <!-- EMC PANE -->
                    <pane id="emcPane" icon="emc.png" :descs="['emcPane_desc']">
                        <card checked="true">
                            <div class="col-12">
                                <div class="row gx-3">
                                    <div class="col">
                                        <div class="small">{{ $t('selectEmcAmount') }}</div>
                                        <select class="form-control" v-model="selectedEmcAmount" @change="setEmcAmount(selectedEmcAmount)">
                                            <option value="max">Max</option>
                                            <option value="1">1</option>
                                            <option value="10">10</option>
                                            <option value="100">100</option>
                                            <option value="1000">{{ numeralFormat(1000, '0a') }}</option>
                                            <option value="10000">{{ numeralFormat(10000, '0a') }}</option>
                                            <option value="100000">{{ numeralFormat(100000, '0a') }}</option>
                                        </select>
                                    </div>
                                    <div v-if="data['autoEmc'].count > 0" class="col">
                                        <div class="small">{{ $t('selectAutoEmcInterval') }}</div>
                                        <select class="form-control" v-model="selectedAutoEmcInterval" @change="setAutoEmcInterval(selectedAutoEmcInterval)">
                                            <option value="1">{{ $t('1second') }}</option>
                                            <option value="10">{{ $t('10second') }}</option>
                                            <option value="60">{{ $t('1minute') }}</option>
                                        </select>
                                    </div>
                                    <div class="col-12 mt-2">
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" id="checkEmcShortcut" v-model="showEmcShortcut" @click="setDisplayEmcShortcut(!showEmcShortcut)" />
                                            <label class="form-check-label small" for="checkEmcShortcut">{{ $t('showEmcShortcut') }}</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </card>
                        <card checked="true">
                            <div class="col-12">
                                <div class="row g-1">
                                    <emc id="emcMeteorite" />
                                    <emc id="emcCarbon" />
                                    <emc id="emcOil" />
                                    <emc id="emcMetal" />
                                    <emc id="emcGem" />
                                    <emc id="emcWood" />
                                    <emc id="emcSilicon" />
                                    <emc id="emcUranium" />
                                    <emc id="emcLava" />
                                    <emc id="emcLunarite" />
                                    <emc id="emcMethane" />
                                    <emc id="emcTitanium" />
                                    <emc id="emcGold" />
                                    <emc id="emcSilver" />
                                    <emc id="emcHydrogen" />
                                    <emc id="emcHelium" />
                                    <emc id="emcIce" />
                                </div>
                            </div>
                        </card>
                    </pane>

                    <!-- DYSON PANE -->
                    <pane id="dysonPane" icon="dyson.png" :descs="['dysonPane_desc']">
                        <buildable id="segment" btnText="build" collapse="true" />
                        <buildable id="dysonT1" btnText="build" collapse="true" />
                        <buildable id="dysonT2" btnText="build" collapse="true" />
                        <buildable id="dysonT3" btnText="build" collapse="true" />
                    </pane>

                    <!-- NANOSWARM PANE -->
                    <pane id="nanoswarmPane" icon="nanoswarm.png">
                        <buildable id="nanoswarm" btnText="build" />
                    </pane>

                    <!-- ANTIMATTER PANE -->
                    <pane id="antimatterPane" icon="antimatter.png" :descs="['antimatterPane_desc']" pinnable="antimatter">
                        <resource id="antimatter" />
                        <buildable id="antimatterT1" btnText="build" />
                    </pane>

                    <!-- COMMUNICATION PANE -->
                    <pane id="communicationPane" icon="communication.png" :descs="['communicationPane_desc']">
                        <buildable id="radarT1" btnText="build" />
                        <buildable id="radarT2" btnText="build" />
                    </pane>

                    <!-- SPACESHIP PANE -->
                    <pane id="spaceshipPane" icon="spaceship.png" :descs="['spaceshipPane_desc']">
                        <buildable id="spaceship" btnText="build" />
                        <buildable id="shield" btnText="build" calc="true" />
                        <buildable id="engine" btnText="build" calc="true" />
                        <buildable id="aero" btnText="build" calc="true" />
                    </pane>

                    <!-- MILITARY PANE -->
                    <pane id="militaryPane" icon="military.png">
                        <fleet id="fleet" />
                        <buildable id="shipT1" btnText="build" />
                        <buildable id="shipT2" btnText="build" />
                        <buildable id="shipT3" btnText="build" />
                        <buildable id="shipT4" btnText="build" />
                        <buildable id="shipT5" btnText="build" />
                    </pane>

                    <!-- TERRAFORMING PANE -->
                    <pane id="terraformingPane" icon="terraforming.png" :descs="['terraformingPane_desc']">
                        <buildable id="probe" btnText="build" />
                        <buildable id="terraformer" btnText="build" />
                    </pane>

                    <!-- INTERSTELLAR CARNELIAN PANE -->
                    <pane id="interstellarCarnelianPane" icon="carnelian.png" :descs="['interstellarCarnelianPane_desc']">
                        <star id="star301"    /> <star id="star163901" /> <star id="star181901" /> <star id="star151801" /> <star id="star25401"  /> <star id="star146301" />
                        <star id="star122601" /> <star id="star79501"  /> <star id="star1501"   /> <star id="star79901"  /> <star id="star37601"  /> <star id="star123401" />
                        <star id="star164301" /> <star id="star219102" /> <star id="star204702" /> <star id="star116901" /> <star id="star74001"  /> <star id="star205102" />
                        <star id="star144001" /> <star id="star222301" /> <star id="star3901"   /> <star id="star168301" /> <star id="star120901" /> <star id="star125301" />
                        <star id="star113101" /> <star id="star89101"  /> <star id="star93901"  /> <star id="star79201"  /> <star id="star80501"  /> <star id="star77301"  />
                        <star id="star191701" /> <star id="star199702" /> <star id="star21001"  /> <star id="star178302" /> <star id="star32201"  /> <star id="star74801"  />
                    </pane>

                    <!-- INTERSTELLAR PRASNIAN PANE -->
                    <pane id="interstellarPrasnianPane" icon="prasnian.png" :descs="['interstellarPrasnianPane_desc']">
                        <star id="star401"    /> <star id="star25101"  /> <star id="star207601" /> <star id="star223901" /> <star id="star121101" /> <star id="star136701" />
                        <star id="star166402" /> <star id="star95001"  /> <star id="star175902" /> <star id="star56501"  /> <star id="star167801" /> <star id="star103201" />
                        <star id="star113301" /> <star id="star199602" /> <star id="star157201" /> <star id="star222201" /> <star id="star6301"   /> <star id="star214301" />
                        <star id="star40801"  /> <star id="star207301" /> <star id="star169601" /> <star id="star157101" /> <star id="star178501" /> <star id="star208601" />
                        <star id="star78101"  /> <star id="star123501" /> <star id="star85901"  /> <star id="star18501"  /> <star id="star199801" /> <star id="star141901" />
                        <star id="star5201"   /> <star id="star223701" /> <star id="star166903" /> <star id="star32101"  /> <star id="star77801"  /> <star id="star205201" />
                    </pane>

                    <!-- INTERSTELLAR HYACINITE PANE -->
                    <pane id="interstellarHyacinitePane" icon="hyacinite.png" :descs="['interstellarHyacinitePane_desc']">
                        <star id="star201"    /> <star id="star217101" /> <star id="star166701" /> <star id="star179501" /> <star id="star6501"   /> <star id="star222401" />
                        <star id="star200001" /> <star id="star24201"  /> <star id="star224202" /> <star id="star92801"  /> <star id="star172701" /> <star id="star86401"  />
                        <star id="star202902" /> <star id="star177001" /> <star id="star68301"  /> <star id="star205001" /> <star id="star13401"  /> <star id="star34201"  />
                        <star id="star182101" /> <star id="star178401" /> <star id="star107601" /> <star id="star192101" /> <star id="star24001"  /> <star id="star16601"  />
                        <star id="star27501"  /> <star id="star121601" /> <star id="star212102" /> <star id="star117501" />
                    </pane>

                    <!-- INTERSTELLAR KITRINOS PANE -->
                    <pane id="interstellarKitrinosPane" icon="kitrinos.png" :descs="['interstellarKitrinosPane_desc']">
                        <star id="star501"    /> <star id="star130601" /> <star id="star158101" /> <star id="star224601" /> <star id="star58601"  /> <star id="star10101"  />
                        <star id="star194201" /> <star id="star1101"   /> <star id="star72501"  /> <star id="star210501" /> <star id="star189701" /> <star id="star175601" />
                        <star id="star206902" /> <star id="star133601" /> <star id="star135801" /> <star id="star39101"  /> <star id="star107001" /> <star id="star105801" />
                        <star id="star224201" /> <star id="star205101" /> <star id="star162501" /> <star id="star4001"   /> <star id="star141101" /> <star id="star180502" />
                        <star id="star208702" /> <star id="star85501"  /> <star id="star217202" /> <star id="star180101" /> <star id="star13801"  /> <star id="star37101"  />
                        <star id="star42501"  /> <star id="star80901"  /> <star id="star215902" /> <star id="star190502" /> <star id="star99701"  /> <star id="star176802" />
                    </pane>

                    <!-- INTERSTELLAR MOVITON PANE -->
                    <pane id="interstellarMovitonPane" icon="moviton.png" :descs="['interstellarMovitonPane_desc']">
                        <star id="star701"    /> <star id="star601"    /> <star id="star80101"  /> <star id="star213301" /> <star id="star13601"  /> <star id="star51801"  />
                        <star id="star35801"  /> <star id="star216801" /> <star id="star224101" /> <star id="star114001" /> <star id="star15301"  /> <star id="star69601"  />
                        <star id="star148501" /> <star id="star155801" /> <star id="star185101" /> <star id="star175901" /> <star id="star203902" /> <star id="star204801" />
                        <star id="star211202" /> <star id="star100801" /> <star id="star124101" /> <star id="star139701" /> <star id="star50401"  /> <star id="star159101" />
                        <star id="star148101" /> <star id="star157301" /> <star id="star72601"  /> <star id="star224801" /> <star id="star71001"  /> <star id="star207501" />
                        <star id="star168302" /> <star id="star128901" /> <star id="star68401"  /> <star id="star30701"  /> <star id="star193402" /> <star id="star84201"  />
                        <star id="star76401"  /> <star id="star32301"  /> <star id="star191401" /> <star id="star118301" /> <star id="star166901" /> <star id="star62901"  />
                        <star id="star21601"  /> <star id="star63801"  /> <star id="star187202" />
                    </pane>

                    <!-- INTERSTELLAR OVERLORD PANE -->
                    <pane id="interstellarOverlordPane" icon="overlord.png" :descs="['interstellarOverlordPane_desc']">
                        <card id="overlordStatues">
                            <div class="col-12">
                                <small>{{ 150 - getStatuesCount }} {{ $t('remainingStatues') }}</small>
                                <div class="progress">
                                    <div class="progress-bar progress-bar-striped progress-bar-animated" :style="'width: ' + ((getStatuesCount / 150) * 100) + '%'">
                                        <div class="small">
                                            <span>{{ (getStatuesCount / 150) * 100 }}%</span>
                                            <span class="ms-1">{{ getStatuesCount }}</span>
                                            <small>/150</small>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 text-end">
                                <button class="btn btn-warning" :class="{ 'disabled':getStatuesCount < 150 }" @click="overlordModal.show()">
                                    {{ $t('meetOverlord') }}
                                </button>
                            </div>
                        </card>
                    </pane>

                    <!-- DARKMATTER PANE -->
                    <pane id="darkmatterPane" icon="darkmatter.png" :descs="['darkmatterPane_desc1', 'darkmatterPane_desc2', 'darkmatterPane_desc3', 'darkmatterPane_desc4', 'darkmatterPane_desc5']">
                        <card id="darkmatter" :descs="['darkmatter_desc']" checked="true">
                            <div class="col-12">
                                <div class="heading-6">{{ $t('dmWonders') }} <span class="text-light">{{ getDMWonders }}</span></div>
                                <div class="small"><span>{{ $t('dmWonders_desc') }}</span></div>
                            </div>
                            <div class="col-12">
                                <div class="heading-6">{{ $t('dmSpheres') }} <span class="text-light">{{ getDMSpheres }}</span></div>
                                <div class="small"><span>{{ $t('dmSpheres_desc') }}</span></div>
                            </div>
                            <div class="col-12">
                                <div class="heading-6">{{ $t('dmResearches') }} <span class="text-light">{{ getDMResearches }}</span></div>
                                <div class="small"><span>{{ $t('dmResearches_desc') }}</span></div>
                            </div>
                            <div class="col-12">
                                <div class="heading-6">{{ $t('dmRank') }} <span class="text-light">{{ getDMRank }}</span></div>
                                <div class="small"><span>{{ $t('dmRank_desc') }}</span></div>
                            </div>
                            <div class="col-12">
                                <div class="heading-6">{{ $t('dmSwarms') }} <span class="text-light">{{ getDMSwarms }}</span></div>
                                <div class="small"><span>{{ $t('dmSwarms_desc') }}</span></div>
                            </div>
                        </card>
                        <card id="rebirth" :descs="['rebirth_desc']" checked="true">
                            <div class="col-12 small">
                                <div class="text-white">{{ $t('rebirth_nb1') }}</div>
                                <div :class="{ 'text-white':data['dysonT3'].count > 0, 'text-danger':data['dysonT3'].count < 1 }">{{ $t('rebirth_nb2') }}</div>
                            </div>
                            <div class="col-12">
                                <div class="row g-1 justify-content-end">
                                    <div class="col-auto">
                                        <button class="btn btn-warning" :class="{ 'disabled':data['dysonT3'].count < 1 }" @click="rebirthModal.show()">{{ $t('rebirth') }}</button>
                                    </div>
                                </div>
                            </div>
                        </card>
                    </pane>

                    <!-- STARGAZE CARNELIAN PANE -->
                    <pane id="stargazeCarnelianPane" icon="carnelian.png" :descs="['stargazeCarnelianPane_desc']">
                        <buildable id="upgradeGain" btnText="activate" />
                        <buildable id="upgradeStorage1" btnText="activate" />
                        <buildable id="upgradeStorage2" btnText="activate" />
                        <buildable id="techEnergyStorage6" btnText="activate" />
                        <buildable id="upgradeStorage3" btnText="activate" />
                    </pane>

                    <!-- STARGAZE PRASNIAN PANE -->
                    <pane id="stargazePrasnianPane" icon="prasnian.png" :descs="['stargazePrasnianPane_desc']">
                        <buildable id="techPlasma3" btnText="activate" />
                        <buildable id="upgradeWonder1" btnText="activate" />
                        <buildable id="techPlasmaStorage3" btnText="activate" />
                        <buildable id="upgradeWonder2" btnText="activate" />
                        <buildable id="upgradeWonder3" btnText="activate" />
                        <buildable id="autoEmc" btnText="activate" />
                        <buildable id="techPlasma4" btnText="activate" />
                    </pane>

                    <!-- STARGAZE HYACINITE PANE -->
                    <pane id="stargazeHyacinitePane" icon="hyacinite.png" :descs="['stargazeHyacinitePane_desc']">
                        <buildable id="upgradeScience1" btnText="activate" />
                        <buildable id="upgradeScience2" btnText="activate" />
                        <buildable id="techScience5" btnText="activate" />
                        <buildable id="upgradeEnergyBoost" btnText="activate" />
                    </pane>

                    <!-- STARGAZE KITRINOS PANE -->
                    <pane id="stargazeKitrinosPane" icon="kitrinos.png" :descs="['stargazeKitrinosPane_desc']">
                        <buildable id="upgradeTier1" btnText="activate" />
                        <buildable id="techEnergyStorage5" btnText="activate" />
                        <buildable id="multiBuy" btnText="activate" />
                        <buildable id="boostCapital" btnText="activate" />
                        <buildable id="techTier5" btnText="activate" />
                    </pane>

                    <!-- STARGAZE MOVITON PANE -->
                    <pane id="stargazeMovitonPane" icon="moviton.png" :descs="['stargazeMovitonPane_desc']">
                        <buildable id="upgradeFuel1" btnText="activate" />
                        <buildable id="upgradeSpaceship" btnText="activate" />
                        <buildable id="techPlasmaStorage4" btnText="activate" />
                        <buildable id="techMeteorite3" btnText="activate" />
                        <buildable id="techMeteorite4" btnText="activate" />
                    </pane>

                    <!-- STARGAZE OVERLORD PANE -->
                    <pane id="stargazeOverlordPane" icon="overlord.png" :descs="['stargazeOverlordPane_desc']">
                        <buildable id="boostDarkmatter" btnText="activate" />
                        <buildable id="upgradeFaction" btnText="activate" />
                    </pane>

                    <!-- ULTRITE PANE -->
                    <pane id="ultritePane" icon="ultrite.png" :descs="['ultritePane_desc1', 'ultritePane_desc2', 'ultritePane_desc3', 'ultritePane_desc4', 'ultritePane_desc5']">
                        <card id="ultrite" :descs="['ultrite_desc']" checked="true">
                            <div class="col-12">
                                <div class="heading-6">{{ $t('ulStars') }} <span class="text-light">{{ getULStars }}</span></div>
                                <div class="small"><span>{{ $t('ulStars_desc') }}</span></div>
                            </div>
                            <div class="col-12">
                                <div class="heading-6">{{ $t('ulDarkmatter') }} <span class="text-light">{{ getULDarkmatter }}</span></div>
                                <div class="small"><span>{{ $t('ulDarkmatter_desc') }}</span></div>
                            </div>
                            <div class="col-12">
                                <div class="heading-6">{{ $t('ulStatues') }} <span class="text-light">{{ getULStatues }}</span></div>
                                <div class="small"><span>{{ $t('ulStatues_desc') }}</span></div>
                            </div>
                        </card>
                        <card id="enlighten" :descs="['enlighten_desc']" checked="true">
                            <div class="col-12 small">
                                <div :class="{ 'text-white':getOwnedStarCount >= 10, 'text-danger':getOwnedStarCount < 10 }">{{ $t('enlighten_nb1') }}</div>
                            </div>
                            <div class="col-12">
                                <div class="row g-1 justify-content-end">
                                    <div class="col-auto">
                                        <button class="btn btn-warning" :class="{ 'disabled':getOwnedStarCount < 10 }" @click="enlightenModal.show()" >{{ $t('enlighten') }}</button>
                                    </div>
                                </div>
                            </div>
                        </card>
                    </pane>

                    <!-- TITANS PANE -->
                    <pane id="titansPane" icon="titans.png" :descs="['titansPane_desc']">
                        <card id="titans" checked="true">
                            <div class="col-12 mt-2">
                                <div class="row g-1">
                                    <div v-for="res in resources" :key="res.id" class="col-4 col-md-2">
                                        <div class="rounded py-2" :class="{ 'opacity-1':!res.titan }" style="background-color:rgba(255,255,255,.125);" role="heading">
                                            <div class="row g-1">
                                                <div class="col-12 text-center">
                                                    <img :src="require(`./assets/interface/${res.id}.png`)" width="24" height="24" />
                                                </div>
                                                <div class="col-12 small text-center">
                                                    <span class="text-light">{{ $t(res.id) }}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </card>
                        <card v-if="titanSwapingCount < 1" id="titanSwaping" checked="true" :descs="['titanSwaping_desc']">
                            <div v-if="getCurrentTitan.length > 0" class="col-12">
                                <small class="text-light">{{ $t('titanSource') }}</small>
                                <select class="form-control" v-model="titanSource">
                                    <option></option>
                                    <option v-for="item in getCurrentTitan" :key="item" :value="item">{{ $t(item) }}</option>
                                </select>
                            </div>
                            <div v-if="getCurrentTitan.length > 0" class="col-12">
                                <small class="text-light">{{ $t('titanDestination') }}</small>
                                <select class="form-control" v-model="titanDestination">
                                    <option></option>
                                    <option v-for="item in getNotCurrentTitan" :key="item" :value="item">{{ $t(item) }}</option>
                                </select>
                            </div>
                            <div v-if="getCurrentTitan.length > 0" class="col-12 text-end">
                                <button class="btn" @click="swapTitan({ 'source':titanSource, 'destination':titanDestination })">
                                    {{ $t('swap') }}
                                </button>
                            </div>
                        </card>
                    </pane>

                    <!-- UPGRADES PANE -->
                    <pane id="upgradesPane" icon="upgrades.png">
                        <buildable id="overlordProgram" btnText="activate" />
                        <buildable id="advUpgradeStorage1" btnText="activate" />
                        <buildable id="shipSpeedEnhancement" btnText="activate" />
                        <buildable id="shipDefenceEnhancement" btnText="activate" />
                        <buildable id="shipPowerEnhancement" btnText="activate" />
                        <buildable id="techAutoStorageUpgrade" btnText="activate" />
                        <buildable id="techNanoswarm0" btnText="activate" />
                    </pane>
                    <!-- DONATING PANE -->
                    <pane id="donatingPane" icon="donating.png" :descs="['donatingPane_desc1', 'donatingPane_desc2']">
                        <card id="donatingPane_desc3" checked="true">
                            <div class="col-12 small">
                                <span>{{ $t('donatingPane_desc5') }}</span>
                            </div>
                            <div class="col-12">
                                <form class="row g-2 justify-content-end align-items-end" action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank">
                                    <input type="hidden" name="cmd" value="_s-xclick">
                                    <input type="hidden" name="hosted_button_id" value="7XYD7SJFKQ8M4">
                                    <div class="col-12 text-end">
                                        <small>{{ $t('donatingPane_desc4') }}</small>
                                    </div>
                                    <div class="col-12 text-end">
                                        <button type="submit" class="btn">
                                            <div class="row gx-2 align-items-center">
                                                <div class="col-auto d-flex align-items-center"><img :src="require('./assets/interface/paypal.png')" width="16" height="16" /></div>
                                                <div class="col-auto">{{ $t('donate') }}</div>
                                            </div>
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </card>
                    </pane>

                    <!-- ACHIEVEMENTS PANE -->
                    <pane id="achievementPane" icon="trophy.png" :descs="['achievementPane_desc']">
                        <card id="currentRank" checked="true">
                            <div class="col-12">
                                <small>{{ rank.level }} - {{ $t('rank_' + rank.level) }}</small>
                                <div class="progress">
                                    <div class="progress-bar progress-bar-striped progress-bar-animated" :style="'width: ' + rank.percent + '%'">
                                        <div class="small">
                                            <span>{{ rank.percent }}%</span>
                                            <span class="ms-1">{{ rank.current }}</span>
                                            <small>/{{ rank.xpNeeded }}</small>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </card>
                        <card id="statistics" checked="true">
                            <div class="col-12">
                                <table class="table">
                                    <tbody>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('startDate') }}</small></td>
                                            <td class="text-end"><small class="text-light">{{ momentFormat(stats.startDate, 'YYYY-MM-DD') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('lastEnlightenDate') }}</small></td>
                                            <td class="text-end"><small class="text-light">{{ momentFormat(stats.lastEnlightenDate, 'YYYY-MM-DD') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('enlightenCount') }}</small></td>
                                            <td class="text-end"><small class="text-light">{{ numeralFormat(stats.enlightenCount, '0a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('lastRebirthDate') }}</small></td>
                                            <td class="text-end"><small class="text-light">{{ momentFormat(stats.lastRebirthDate, 'YYYY-MM-DD') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('rebirthCount') }}</small></td>
                                            <td class="text-end"><small class="text-light">{{ numeralFormat(stats.rebirthCount, '0a') }}</small></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="col-12">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <td></td>
                                            <td width="1%" nowrap class="text-end"><small>{{ $t('current') }}</small></td>
                                            <td width="1%" nowrap class="text-end"><small>{{ $t('allTime') }}</small></td>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('ultrite') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(data['ultrite'].count.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.allTimeUltrite.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('darkmatter') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(data['darkmatter'].count.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.allTimeDarkmatter.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('manualGain') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.manualGain.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.manualGain.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('machineT1') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT1.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT1.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('machineT2') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT2.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT2.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('machineT3') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT3.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT3.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('machineT4') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT4.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT4.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('machineT5') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT5.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT5.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('machineT6') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT6.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.machineT6.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('ships') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.ships.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.ships.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                        <tr>
                                            <td><small class="text-normal">{{ $t('starOwned') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.starOwned.current.toPrecision(4), '0.[000]a') }}</small></td>
                                            <td class="text-end"><small class="text-light text-uppercase">{{ numeralFormat(stats.starOwned.allTime.toPrecision(4), '0.[000]a') }}</small></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </card>
                        <card id="resources" checked="true">
                            <div class="col-12 mt-2">
                                <div class="row g-1">
                                    <div v-for="ach in resAchievements" :key="ach.id" class="col-12 col-md-4">
                                        <div class="rounded px-3 py-2" :class="{ 'opacity-1':!ach.unlocked }" style="background-color:rgba(255,255,255,.125);" role="heading">
                                            <div class="row g-1">
                                                <div class="col-12 small">
                                                    <div class="row gx-2">
                                                        <div class="col-auto d-flex align-items-center">
                                                            <img :src="require(`./assets/interface/${ach.icon}`)" width="16" height="16" />
                                                        </div>
                                                        <div class="col-auto">
                                                            <span class="h6 text-light">{{ $t(ach.data) }}</span>
                                                        </div>
                                                        <div v-if="!ach.unlocked" class="col">
                                                            <span class="text-normal">{{ $t('locked') }}</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-12 small">
                                                    <div class="row g-1 mb-2">
                                                        <div v-for="(bracket, index) in ach.brackets" :key="bracket" class="col">
                                                            <small class="text-uppercase" :class="{ 'text-success':ach.count > index, 'text-timer':ach.count == index, 'text-muted':ach.count < index }">{{ numeralFormat(bracket, '0a') }}</small>
                                                            <div class="progress rounded" style="height:3px">
                                                                <div v-if="ach.count > index" class="progress-bar bg-success" style="width:100%"></div>
                                                                <div v-if="ach.count == index" class="progress-bar bg-timer" :style="'width:' + ach.progress + '%'"></div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </card>
                        <card id="producers" checked="true">
                            <div class="col-12 mt-2">
                                <div class="row g-1">
                                    <div v-for="ach in prodAchievements" :key="ach.id" class="col-12 col-md-4">
                                        <div class="rounded px-3 py-2" :class="{ 'opacity-1':!ach.unlocked }" style="background-color:rgba(255,255,255,.125);" role="heading">
                                            <div class="row g-1">
                                                <div class="col-12 small">
                                                    <div class="row gx-2">
                                                        <div class="col-auto d-flex align-items-center">
                                                            <img :src="require(`./assets/interface/${ach.icon}`)" width="16" height="16" />
                                                        </div>
                                                        <div class="col text-truncate">
                                                            <span class="h6 text-light">{{ $t(ach.data) }}</span>
                                                        </div>
                                                        <div v-if="!ach.unlocked" class="col-auto">
                                                            <span class="text-normal">{{ $t('locked') }}</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-12 small">
                                                    <div class="row g-1 mb-2">
                                                        <div v-for="(bracket, index) in ach.brackets" :key="bracket" class="col">
                                                            <small class="text-uppercase" :class="{ 'text-success':ach.count > index, 'text-timer':ach.count == index, 'text-muted':ach.count < index }">{{ numeralFormat(bracket, '0a') }}</small>
                                                            <div class="progress rounded" style="height:3px">
                                                                <div v-if="ach.count > index" class="progress-bar bg-success" style="width:100%"></div>
                                                                <div v-if="ach.count == index" class="progress-bar bg-timer" :style="'width:' + ach.progress + '%'"></div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </card>
                    </pane>

                    <!-- HELP PANE -->
                    <pane id="helpPane" icon="help.png" :descs="['helpPane_desc']">
                        <card id="helpStep1Title" :descs="['helpStep1Text1']" :checked="data['science'].unlocked == true">
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep1Tip1') }}
                                </div>
                            </div>
                        </card>
                        <card v-if="data['science'].unlocked == true" id="helpStep2Title" :descs="['helpStep2Text1']" :checked="data['wonderPrecious0'].unlocked == true">
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep2Tip1') }}
                                </div>
                            </div>
                        </card>
                        <card v-if="data['wonderPrecious0'].unlocked == true" id="helpStep3Title" :descs="['helpStep3Text1']" :checked="data['techDyson0'].unlocked == true">
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep3Tip1') }}
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep3Tip2') }}
                                </div>
                            </div>
                        </card>
                        <card v-if="data['techDyson0'].unlocked == true" id="helpStep4Title" :descs="['helpStep4Text1']" :checked="data['segment'].unlocked == true">
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep4Tip1') }}
                                </div>
                            </div>
                        </card>
                        <card v-if="data['segment'].unlocked == true" id="helpStep5Title" :descs="['helpStep5Text1']" :checked="data['antimatter'].unlocked == true">
                        </card>
                        <card v-if="data['antimatter'].unlocked == true" id="helpStep6Title" :descs="['helpStep6Text1']" :checked="data['segment'].unlocked == true">
                        </card>
                        <card v-if="data['ultrite'].unlocked == true" id="helpStep7Title" :descs="['helpStep7Text1']" :checked="data['ultrite'].unlocked == true">
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep7Tip1') }}
                                </div>
                            </div>
                        </card>
                        <card v-if="data['ultrite'].unlocked == true" id="helpStep8Title" :descs="['helpStep8Text1']">
                            <div class="col-12">
                                <div class="tip tip-normal">
                                    <b class="text-uppercase">{{ $t('tip') }}</b>
                                    {{ $t('helpStep8Tip1') }}
                                </div>
                            </div>
                        </card>
                    </pane>

                    <!-- OPTIONS PANE -->
                    <pane id="settingsPane" icon="cog.png" :descs="['settingsPane_desc']">
                        <card id="companyName" checked="true">
                            <div class="col-12">
                                <div class="row g-1">
                                    <div class="col">
                                        <input type="text" class="form-control" v-model="newCompanyName" />
                                    </div>
                                    <div class="col-auto">
                                        <button class="btn" @click="setCompanyName(newCompanyName)">{{ $t('change') }}</button>
                                    </div>
                                </div>
                            </div>
                        </card>
                        <card id="importExport" checked="true">
                            <div class="col-12">
                                <div class="row g-1">
                                    <div class="col-auto">
                                        <button class="btn" @click="exportData()">{{ $t('export') }}</button>
                                    </div>
                                    <div class="col-auto">
                                        <button class="btn" @click="importData()">{{ $t('import') }}</button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <textarea class="form-control" style="height:100px;" v-model="compressed"></textarea>
                            </div>
                            <div class="col-12 small">
                                <span>{{ $t('importExport_desc') }}</span>
                            </div>
                        </card>
                        <card id="notifications" checked="true">
                            <div class="col-12">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="checkRoadmap" v-model="showRoadmap" @click="setDisplayRoadmap(!showRoadmap)" />
                                    <label class="form-check-label small" for="checkRoadmap">{{ $t('showRoadmap') }}</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="checkPinnedItems" v-model="showPinnedItems" @click="setDisplayPinnedItems(!showPinnedItems)" />
                                    <label class="form-check-label small" for="checkPinnedItems">{{ $t('showPinnedItems') }}</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="checkDoneTechs" v-model="showDoneTechs" @click="setDisplayDoneTechs(!showDoneTechs)" />
                                    <label class="form-check-label small" for="checkDoneTechs">{{ $t('showDoneTechs') }}</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="checkHideLocked" v-model="showLockedItems" @click="setDisplayLockedItems(!showLockedItems)" />
                                    <label class="form-check-label small" for="checkHideLocked">{{ $t('showLockedItems') }}</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="checkToastAutoSave" v-model="showToastAutoSave" @click="setNotifAutoSave(!showToastAutoSave)" />
                                    <label class="form-check-label small" for="checkToastAutoSave">{{ $t('showToastAutoSave') }}</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="checkToastAchievement" v-model="showToastAchievement" @click="setNotifAchievement(!showToastAchievement)" />
                                    <label class="form-check-label small" for="checkToastAchievement">{{ $t('showToastAchievement') }}</label>
                                </div>
                            </div>
                        </card>
                        <card id="saving" checked="true">
                            <div class="col-12">
                                <div class="mb-1">
                                    <small>{{ $t('autoSavingDuration') }}</small>
                                </div>
                                <div>
                                    <select class="form-control" v-model="autoSavingDuration" @change="setAutoSaveInterval(autoSavingDuration)">
                                        <option value="30">{{ $t('30seconds') }}</option>
                                        <option value="120">{{ $t('2minutes') }}</option>
                                        <option value="600">{{ $t('10minutes') }}</option>
                                        <option value="-1">{{ $t('off') }}</option>
                                    </select>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="mb-1">
                                    <small>{{ $t('manualSaving') }}</small>
                                </div>
                                <div class="row g-1">
                                    <div class="col-auto">
                                        <button class="btn" @click="onSave()">
                                            {{ $t('save') }}
                                        </button>
                                    </div>
                                    <div class="col text-end">
                                        <button class="btn btn-danger" @click="hardResetModal.show();">
                                            <span class="text-danger">{{ $t('hardReset') }}</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </card>
                    </pane>

                    <!-- ABOUT PANE -->
                    <pane id="aboutPane" icon="about.png" :descs="['aboutPane_desc']">
                        <card id="about1" :descs="['about1_desc1']" checked="true">
                            <div class="col-12 small">
                                <ul class="mb-2">
                                    <li class="text-truncate">
                                        <span class="text-light me-2">NG Site</span>
                                        <a href="https://ngspacecompany.exileng.com/">https://ngspacecompany.exileng.com/</a>
                                    </li>
                                    <li class="text-truncate">
                                        <span class="text-light me-2">NG Github</span>
                                        <a href="https://github.com/ExileNG/NGSpaceCompany" target="_blank">https://github.com/ExileNG/NGSpaceCompany</a>
                                    </li>
                                    <li class="text-truncate">
                                        <span class="text-light me-2">NG Discord</span>
                                        <a href="https://discord.gg/3UkgeeT9CV" target="_blank">https://discord.gg/3UkgeeT9CV</a>
                                    </li>
                                </ul>
                                <ul class="mb-0">
                                    <li class="text-truncate">
                                        <span class="text-light me-2">Original Site</span>
                                        <a href="https://sparticle999.github.io/spacecompany" target="_blank">https://sparticle999.github.io/spacecompany</a>
                                    </li>
                                    <li class="text-truncate">
                                        <span class="text-light me-2">Original Github</span>
                                        <a href="https://github.com/sparticle999/SpaceCompany" target="_blank">https://github.com/sparticle999/SpaceCompany</a>
                                    </li>
                                    <li class="text-truncate">
                                        <span class="text-light me-2">Original Discord</span>
                                        <a href="https://discord.gg/hgRUjVp" target="_blank">https://discord.gg/hgRUjVp</a>
                                    </li>
                                </ul>
                            </div>
                        </card>
                        <card id="about4" checked="true">
                            <div class="col-12">
                                <div class="row gy-1 gx-3">
                                    <div class="col-auto"><small class="text-donor">Beric01</small></div>
                                    <div class="col-auto"><small class="text-donor">Malchron</small></div>
                                    <div class="col-auto"><small class="text-donor">Nisse</small></div>
                                    <div class="col-auto"><small class="text-donor">McFloppy</small></div>
                                    <div class="col-auto"><small class="text-donor">Kirri</small></div>
                                    <div class="col-auto"><small class="text-donor">Automaton_2000</small></div>
                                    <div class="col-auto"><small class="text-donor">Gar the Blind Chipmunk</small></div>
                                    <div class="col-auto"><small class="text-donor">Aegis</small></div>
                                    <div class="col-auto"><small class="text-donor">FatBlock</small></div>
                                </div>
                            </div>
                        </card>
                        <card id="about2" checked="true">
                            <div class="col-12">
                                <div class="row gy-1 gx-3">
                                    <div class="col-auto"><small class="text-timer">darklord192</small></div>
                                    <div class="col-auto"><small class="text-timer">freeed</small></div>
                                    <div class="col-auto"><small class="text-timer">Daffson</small></div>
                                    <div class="col-auto"><small class="text-timer">PeterO</small></div>
                                    <div class="col-auto"><small class="text-timer">Tamash</small></div>
                                </div>
                            </div>
                        </card>
                        <card id="about3" checked="true">
                            <div class="col-12 small">{{ $t('about3_desc1') }} <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
                            <div class="col-12 small">
                                <ul class="mb-0">
                                    <li>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a></li>
                                </ul>
                            </div>
                        </card>
                    </pane>

                    <!-- RANK PANE -->
                    <pane id="rankPane" icon="rank.png" :descs="['rankPane_desc']">
                        <card id="account" :checked="token != null">
                            <div v-if="token" class="col-12">
                                <div class="row gx-3 gy-2 align-items-center">
                                    <div class="col-12 col-md-auto small">
                                        <span>{{ $t('connected') }} <span class="text-light">{{ username }}</span></span>
                                    </div>
                                    <div class="col-12 col-md-auto text-end">
                                        <button class="btn" @click="onDisconnect()">{{ $t('disconnect') }}</button>
                                    </div>
                                </div>
                            </div>
                            <div v-if="!token" class="col-12">
                                <div class="row gx-3 gy-2 align-items-end">
                                    <div class="col-12 small">
                                        <span>{{ $t('account_desc') }}</span>
                                    </div>
                                    <div class="col-12 col-md-auto">
                                        <small>{{ $t('login') }}</small>
                                        <input type="text" class="form-control" v-model="login" />
                                    </div>
                                    <div class="col-12 col-md-auto">
                                        <small>{{ $t('password') }}</small>
                                        <input type="password" class="form-control" v-model="password" />
                                    </div>
                                    <div class="col-12 col-md-auto text-end">
                                        <button class="btn" @click="onConnect(login, password)">{{ $t('connect') }}</button>
                                    </div>
                                </div>
                            </div>
                        </card>
                        <card v-if="!leaderboard_ranks" :descs="['rankPane_nodata']">
                        </card>
                        <card v-if="leaderboard_ranks" :checked="token != null">
                            <div class="row g-1">
                                <div v-for="(item, index) in leaderboard_stats" :key="item.user_id" class="col-12 col-md-4">
                                    <div class="btn text-start w-100" :class="{ 'border-success':item.username==username }">
                                        <div class="row g-0">
                                            <div class="col-12 mb-2">
                                                <div class="row gx-2">
                                                    <div class="col text-truncate">
                                                        <span class="h6 text-light">{{ item.username }}</span>
                                                    </div>
                                                    <div class="col-auto">
                                                        <span class="text-light d-inline w-100 text-truncate">{{ index + 1 }}</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-12 small">
                                                <div class="row gx-2">
                                                    <div class="col">
                                                        <span class="text-muted">{{ $t('statsUltrite') }}</span>
                                                    </div>
                                                    <div class="col-auto">
                                                        <span class="text-normal">{{ numeralFormat(item.ultrite) }}</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-12 small">
                                                <div class="row gx-2">
                                                    <div class="col">
                                                        <span class="text-muted">{{ $t('statsDarkmatter') }}</span>
                                                    </div>
                                                    <div class="col-auto">
                                                        <span class="text-normal">{{ numeralFormat(item.darkmatter) }}</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-12 small">
                                                <div class="row gx-2">
                                                    <div class="col">
                                                        <span class="text-muted">{{ $t('statsXP') }}</span>
                                                    </div>
                                                    <div class="col-auto">
                                                        <span class="text-normal">{{ numeralFormat(item.xp) }}</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </card>
                    </pane>

                </div>
            </inner-content>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 me-2">

            <!-- SAVING TOAST -->
            <div id="toastAutoSave" class="toast hide fade bg-info" role="alert">
                <div class="toast-body text-dark">
                    <div class="row">
                        <div class="col">
                            <strong>{{ $t('toastAutoSave_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="small">{{ $t('toastAutoSave_text') }}</div>
                </div>
            </div>

            <!-- ACHIEVEMENT TOAST -->
            <div id="toastAchievement" class="toast hide fade bg-success cursor-hover" role="alert">
                <div class="toast-body text-light">
                    <div class="row">
                        <div class="col" @click="setActivePane('achievementPane')" >
                            <strong>{{ $t('toastAchievement_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" ></button>
                        </div>
                    </div>
                    <div class="small" @click="setActivePane('achievementPane')" >{{ $t('toastAchievement_text') }}</div>
                </div>
            </div>

            <!-- SPY TOAST -->
            <div id="toastSpySuccess" class="toast hide fade bg-success" role="alert">
                <div class="toast-body text-light">
                    <div class="row">
                        <div class="col">
                            <strong>{{ $t('toastSpySuccess_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="small">{{ $t('toastSpySuccess_text') }}</div>
                </div>
            </div>
            <div id="toastSpyFailed" class="toast hide fade bg-danger" role="alert">
                <div class="toast-body text-light">
                    <div class="row">
                        <div class="col">
                            <strong>{{ $t('toastSpyFailed_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="small">{{ $t('toastSpyFailed_text') }}</div>
                </div>
            </div>

            <!-- INVADE TOAST -->
            <div id="toastInvadeSuccess" class="toast hide fade bg-success" role="alert">
                <div class="toast-body text-light">
                    <div class="row">
                        <div class="col">
                            <strong>{{ $t('toastInvadeSuccess_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="small">{{ $t('toastInvadeSuccess_text') }}</div>
                </div>
            </div>
            <div id="toastInvadeFailed" class="toast hide fade bg-danger" role="alert">
                <div class="toast-body text-light">
                    <div class="row">
                        <div class="col">
                            <strong>{{ $t('toastInvadeFailed_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="small">{{ $t('toastInvadeFailed_text') }}</div>
                </div>
            </div>

            <!-- ABSORB TOAST -->
            <div id="toastAbsorbSuccess" class="toast hide fade bg-success" role="alert">
                <div class="toast-body text-light">
                    <div class="row">
                        <div class="col">
                            <strong>{{ $t('toastAbsorbSuccess_title') }}</strong>
                        </div>
                        <div class="col-auto">
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                    </div>
                    <div class="small">{{ $t('toastAbsorbSuccess_text') }}</div>
                </div>
            </div>

        </div>
    </div>

    <!-- SPY MODAL -->
    <div v-if="loaded" id="spyModal" class="modal fade">
        <div class="modal-dialog" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-light">{{ $t('spy') }} {{ $t(activeStar) }}</span>
                        </div>
                        <div class="col-12 small">
                            <span class="text-normal">{{ $t('spy_desc') }}</span>
                        </div>
                        <div class="col-12">
                            <div class="row g-2">
                                <div class="col small">
                                    <div class="text-normal">{{ $t('threat') }}</div>
                                    <div class="text-light">{{ $t('threat' + getThreat(activeStar)) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('power') }}</div>
                                    <div class="text-light">{{ getStarPower(activeStar) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('defense') }}</div>
                                    <div class="text-light">{{ getStarDefense(activeStar) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('speed') }}</div>
                                    <div class="text-light">{{ getStarSpeed(activeStar) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('chance') }}</div>
                                    <div class="text-light">{{ numeralFormat(getSpyChance(activeStar), '0') }}%</div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="row g-2 align-items-center">
                                <div class="col">
                                    <small class="text-normal">{{ $t('shipT1') }}</small>
                                </div>
                                <div class="col-auto">
                                    <span class="text-light">{{ data['shipT1'].active }}</span>
                                    <small class="ms-1 text-normal">/{{ data['shipT1'].count }}</small>
                                </div>
                                <div class="col-auto">
                                    <div class="btn-group">
                                        <button class="btn p-1" @click="setActiveShip({ id:'shipT1', count:1 })">
                                            +
                                        </button>
                                        <button class="btn p-1" @click="setActiveShip({ id:'shipT1', count:'max' })">
                                            ++
                                        </button>
                                    </div>
                                </div>
                                <div class="col-auto">
                                    <div class="btn-group">
                                        <button class="btn p-1" @click="setActiveShip({ id:'shipT1', count:-1 })">
                                            -
                                        </button>
                                        <button class="btn p-1" @click="setActiveShip({ id:'shipT1', count:'none' })">
                                            --
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="row g-2 justify-content-end">
                                <div class="col-auto">
                                    <button class="btn" @click="onSpy()" data-bs-dismiss="modal">
                                        {{ $t('spy') }}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- INVADE MODAL -->
    <div v-if="loaded" id="invadeModal" class="modal fade">
        <div class="modal-dialog" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-light">{{ $t('invade') }} {{ $t(activeStar) }}</span>
                        </div>
                        <div class="col-12 small">
                            <span class="text-normal">{{ $t('invade_desc') }}</span>
                        </div>
                        <div class="col-12">
                            <div class="row g-2">
                                <div class="col small">
                                    <div class="text-normal">{{ $t('threat') }}</div>
                                    <div class="text-light">{{ $t('threat' + getThreat(activeStar)) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('power') }}</div>
                                    <div class="text-light">{{ getStarPower(activeStar) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('defense') }}</div>
                                    <div class="text-light">{{ getStarDefense(activeStar) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('speed') }}</div>
                                    <div class="text-light">{{ getStarSpeed(activeStar) }}</div>
                                </div>
                                <div class="col small">
                                    <div class="text-normal">{{ $t('chance') }}</div>
                                    <div v-if="data[activeStar].spy <= 2" class="text-light">???</div>
                                    <div v-if="data[activeStar].spy > 2" class="text-light">{{ Math.round(getInvadeChance(activeStar) * 100) }}%</div>
                                </div>
                            </div>
                        </div>
                        <div v-for="shipId in ['shipT1', 'shipT2', 'shipT3', 'shipT4', 'shipT5']" :key="shipId" class="col-12">
                            <div class="row g-2 align-items-center">
                                <div class="col">
                                    <small class="text-normal">{{ $t(shipId) }}</small>
                                </div>
                                <div class="col-auto">
                                    <span class="text-light">{{ data[shipId].active }}</span>
                                    <small class="ms-1 text-normal">/{{ data[shipId].count }}</small>
                                </div>
                                <div class="col-auto">
                                    <div class="btn-group">
                                        <button class="btn p-1" @click="setActiveShip({ id:shipId, count:1 })">
                                            +
                                        </button>
                                        <button class="btn p-1" @click="setActiveShip({ id:shipId, count:'max' })">
                                            ++
                                        </button>
                                    </div>
                                </div>
                                <div class="col-auto">
                                    <div class="btn-group">
                                        <button class="btn p-1" @click="setActiveShip({ id:shipId, count:-1 })">
                                            -
                                        </button>
                                        <button class="btn p-1" @click="setActiveShip({ id:shipId, count:'none' })">
                                            --
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="row g-2 justify-content-end">
                                <div class="col-auto">
                                    <button class="btn" @click="onInvade()" data-bs-dismiss="modal">
                                        {{ $t('invade') }}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ABSORB MODAL -->
    <div v-if="loaded" id="absorbModal" class="modal fade">
        <div class="modal-dialog" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-light">{{ $t('absorb') }} {{ $t(activeStar) }}</span>
                        </div>
                        <div class="col-12 small">
                            <span class="text-normal">{{ $t('absorb_desc') }}</span>
                        </div>
                        <div class="col-12">
                            <div class="row g-2 justify-content-end">
                                <div class="col-auto">
                                    <button class="btn" @click="onAbsorb()" data-bs-dismiss="modal">
                                        {{ $t('absorb') }}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- REBIRTH MODAL -->
    <div v-if="loaded" id="rebirthModal" class="modal fade">
        <div class="modal-dialog" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-light">{{ $t('rebirth') }}</span>
                        </div>
                        <div class="col-12 small">
                            <span class="text-normal">{{ $t('rebirth_confirm') }}</span>
                        </div>
                        <div class="col-12 text-end">
                            <button class="btn btn-warning" @click="onRebirth()">{{ $t('rebirth') }}</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ENLIGHTEN MODAL -->
    <div v-if="loaded" id="enlightenModal" class="modal fade">
        <div class="modal-dialog" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-light">{{ $t('enlighten') }}</span>
                        </div>
                        <div class="col-12">
                            <small>{{ $t('titanChoice') }}</small>
                            <select class="form-control" v-model="enlightenSelected">
                                <option v-for="res in resources" :key="res.id" :value="res.id">{{ $t(res.id) }} <span v-if="res.titan == true" >{{ $t('alreadyActivated') }}</span></option>
                            </select>
                        </div>
                        <div class="col-12 small">
                            <span class="text-normal">{{ $t('enlighten_confirm') }}</span>
                        </div>
                        <div class="col-12 text-end">
                            <button class="btn btn-warning" @click="onEnlighten()">{{ $t('enlighten') }}</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- HARD RESET MODAL -->
    <div v-if="loaded" id="hardResetModal" class="modal fade">
        <div class="modal-dialog modal-dialog-scrollable" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-light">{{ $t('hardReset') }}</span>
                        </div>
                        <div class="col-12 small">
                            <span class="text-normal">{{ $t('hardReset_confirm') }}</span>
                        </div>
                        <div class="col-12 text-end">
                            <button class="btn btn-danger" @click="onHardReset()"><span class="text-danger">{{ $t('hardReset') }}</span></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SEGMENT MODAL -->
    <div v-if="loaded" id="segmentModal" class="modal fade">
        <div class="modal-dialog modal-dialog-scrollable" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <div class="row g-1 align-items-center">
                                <div class="col">
                                    <span class="h6 text-light">{{ $t('segmentModal') }}</span>
                                </div>
                                <div class="col-auto">
                                    <button class="btn" data-bs-dismiss="modal" aria-label="Close">
                                        <i class="fas fa-fw fa-times"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <calc-segment />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- CALC MODAL -->
    <div v-if="loaded" id="calcModal" class="modal fade">
        <div class="modal-dialog modal-dialog-scrollable" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <div class="row g-1 align-items-center">
                                <div class="col">
                                    <span class="h6 text-light">{{ $t(calcId) }} {{ $t('calcModal') }}</span>
                                </div>
                                <div class="col-auto">
                                    <button class="btn" data-bs-dismiss="modal" aria-label="Close">
                                        <i class="fas fa-fw fa-times"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <calc-building :id="calcId" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- OVERLORD MODAL -->
    <div v-if="loaded" id="overlordModal" class="modal fade">
        <div class="modal-dialog modal-dialog-scrollable" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div v-if="defeat != true" class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-normal">{{ $t('overlordModal') }}</span>
                        </div>
                        <div class="col-12">
                            <span class="text-light">{{ $t('overlordModal_text1') }}</span>
                        </div>
                        <div class="col-12 text-end">
                            <button class="btn" @click="defeat = true">{{ $t('next') }}</button>
                        </div>
                    </div>
                    <div v-if="defeat == true" class="row g-2">
                        <div class="col-12">
                            <span class="h6 text-normal">{{ $t('overlordModal') }}</span>
                        </div>
                        <div class="col-12">
                            <span class="text-light">{{ $t('overlordModal_text2') }}</span>
                        </div>
                        <div class="col-12">
                            <span class="text-light">{{ $t('overlordModal_text3') }}</span>
                        </div>
                        <div class="col-12 text-end">
                            <button class="btn" data-bs-dismiss="modal" aria-label="Close">{{ $t('endOfGame') }}</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- CHANGELOG MODAL -->
    <div v-if="loaded" id="changeLogModal" class="modal fade">
        <div class="modal-dialog modal-dialog-scrollable" role="dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row g-2">
                        <div class="col-12">
                            <div class="row g-1 align-items-center">
                                <div class="col">
                                    <span class="h6 text-light">{{ $t('changeLog') }}</span>
                                </div>
                                <div class="col-auto">
                                    <button class="btn" data-bs-dismiss="modal" aria-label="Close">
                                        <i class="fas fa-fw fa-times"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.29.1 - 2021-07-21</div>
                            <ul class="small">
                                <li>FIX: now option in EMC pane to display EMC shortcut on upgrade storage card is taken into account (made by eliannelavoie)</li>
                                <li>FIX: now EMC shortcut on upgrade storage card is hidden if EMC is unlocked (made by eliannelavoie)</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.29.0 - 2021-07-21</div>
                            <ul class="small">
                                <li>FIX: now upgrade storage button is displayed on pinned resource (made by eliannelavoie)</li>
                                <li>NEW: option in EMC pane to display EMC shortcut on upgrade storage card (made by eliannelavoie)</li>
                                <li>NEW: EMC shortcut on upgrade storage card is displayed to convert resource (made by eliannelavoie)</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.6 - 2021-07-19</div>
                            <ul class="small">
                                <li>FIX: now overlord statues progress bar is displayed well</li>
                                <li>FIX: now padding to display scroll bar on left side pane is larger</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.5 - 2021-07-18</div>
                            <ul class="small">
                                <li>FIX: (again) now bribery remains after rebirth and enlightenment</li>
                                <li>FIX: now hydrogen, helium, and ice can be unlocked in any order</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.4 - 2021-07-16</div>
                            <ul class="small">
                                <li>FIX: now bribery remains after rebirth and enlightenment</li>
                                <li>FIX: now empty storage timer displays '> 48h'</li>
                                <li>FIX: now QRS is taken into account in achievements</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.3 - 2021-07-15</div>
                            <ul class="small">
                                <li>FIX: now invade chance computing is fixed</li>
                                <li>FIX: now dyson segment and items are collapsable</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.2 - 2021-07-13</div>
                            <ul class="small">
                                <li>FIX: now EMC interval is saved and loaded</li>
                                <li>FIX: now antimatter is purple when affected by rift</li>
                                <li>FIX: now antimatter indicates the time taken for full storage</li>
                                <li>FIX: now rift is taken into account for auto-storage</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.1 - 2021-07-12</div>
                            <ul class="small">
                                <li>FIX: spaceship parts cannot be built if spaceship is already built</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.28.0 - 2021-07-12</div>
                            <ul class="small">
                                <li>FIX: spaceship parts cannot be built if spaceship is already built</li>
                                <li>FIX: nanoswarm is not applied on consumption</li>
                                <li>FIX: added close button on calculators</li>
                                <li>FIX: option to show roadmap and done techs are saved</li>
                                <li>FIX: T5 machines unlocked if meteorite wonder is already activated</li>
                                <li>FIX: auto-storage occurs when storage is full (rift is not taken into account)</li>
                                <li>NEW: grey out the enlighten button if you don't have 1à conquered stars at least</li>
                                <li>NEW: grey out the titan swapping button if you don't have any titan</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.27.1 - 2021-07-09</div>
                            <ul class="small">
                                <li>FIX: QoL DM upgrades are locked after enlighenment</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.27.0 - 2021-07-09</div>
                            <ul class="small">
                                <li>FIX: now auto emc is working fine in background</li>
                                <li>FIX: chemical plant boost is applied on production only</li>
                                <li>FIX: some typos (thx to silent1b)</li>
                                <li>NEW: option to show/hide the Overlord roadmap</li>
                                <li>NEW: QoL DM upgrades are not reset after enlighenment</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.26.1 - 2021-07-08</div>
                            <ul class="small">
                                <li>FIX: various accessibility issues</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.26.0 - 2021-07-08</div>
                            <ul class="small">
                                <li>FIX: compute costs after titan swaping</li>
                                <li>FIX: building calculator costs were wrong</li>
                                <li>NEW: overlord roadmap to conquer the universe</li>
                                <li>NEW: option to display/hide researched techs</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.25.0 - 2021-07-07</div>
                            <ul class="small">
                                <li>FIX: hard reset does nothing</li>
                                <li>FIX: ship costs computed after failed invasion</li>
                                <li>NEW: added titan swaping ability</li>
                                <li>NEW: grey out the rebirth button when you can't rebirth yet</li>
                                <li>NEW: added plasma storage tier 4 + moviton dark matter upgrade to unlock it</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.24.0 - 2021-07-06</div>
                            <ul class="small">
                                <li>FIX: dimension rift is taken into account in wonder costs</li>
                                <li>FIX: dimension rift is taken into account in calculators</li>
                                <li>CHANGE: updated ways to gain ultrite</li>
                                <li>NEW: added calculators on spaceship parts</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.23.0 - 2021-07-05</div>
                            <ul class="small">
                                <li>FIX: nanoswarm pane is displayed</li>
                                <li>NEW: close button in change log modal</li>
                                <li>NEW: overlord appreciation program as ultrite upgrade</li>
                                <li>NEW: terraforming ships</li>
                                <li>NEW: overloard statues</li>
                                <li>NEW: the end of the game</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.22.0 - 2021-07-02</div>
                            <ul class="small">
                                <li>FIX: auto-storage upgrade works on all resources (again)</li>
                                <li>FIX: display storage upgrade button only when tech storage is done</li>
                                <li>FIX: removed tooltip on storage upgrade button on left side</li>
                                <li>CHANGE: updated cost of nanoswarm and auto upgrade storage ultrite prices</li>
                                <li>NEW: display resource count in specific color when your store resource in another dimension</li>
                                <li>NEW: advanced storage discount ultrite upgrade</li>
                                <li>NEW: 3 ship enhancement ultrite upgrades</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.21.0 - 2021-07-02</div>
                            <ul class="small">
                                <li>FIX: now quasar redirection system is working well</li>
                                <li>FIX: dimensional rift is taken into account in storage cap displaying</li>
                                <li>FIX: dimensional rift is taken into account in EMC</li>
                                <li>FIX: multy-buy buttons are displayed on 1 row</li>
                                <li>FIX: auto-storage upgrade works on all resources</li>
                                <li>NEW: small button to upgrade storage in left side menu</li>
                                <li>NEW: dyson items achievements</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.20.3 - 2021-07-01</div>
                            <ul class="small">
                                <li>FIX: fixed issue with data exporting</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.20.2 - 2021-07-01</div>
                            <ul class="small">
                                <li>FIX: invading and absorbtion are initially allowed but invade chance is displayed when star is spyied only</li>
                                <li>FIX: save in local storage a crypted copy of data</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.20.1 - 2021-07-01</div>
                            <ul class="small">
                                <li>FIX: now auto storage upgrade ultrite upgrade is displayed after enlightenment</li>
                                <li>FIX: typo in enlightenment modal</li>
                                <li>FIX: dimensional rift is taken into account in timer computing</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.20.0 - 2021-06-30</div>
                            <ul class="small">
                                <li>FIX: now segment and machine calculators take titans into account</li>
                                <li>NEW: change leaderboard ranking to take into account ultrite and darkmatter</li>
                                <li>NEW: now you could pin resoure pane to have them displaued in top of left menu ; must be activated in options menu</li>
                                <li>NEW: now you could build dyson items in one click</li>
                                <li>NEW: auto storage upgrade ultrite upgrade</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.19.0 - 2021-06-29</div>
                            <ul class="small">
                                <li>FIX: EMC convert to full storage</li>
                                <li>FIX: star stats are fixed number</li>
                                <li>NEW: click on update version button trigger a manual save</li>
                                <li>NEW: now you have to spy before invading</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.18.1 - 2021-06-28</div>
                            <ul class="small">
                                <li>FIX: stats loading</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.18.0 - 2021-06-28</div>
                            <ul class="small">
                                <li>NEW: initial implementation of 'Enlightenment' = second layer of prestige</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.17.0 - 2021-06-26</div>
                            <ul class="small">
                                <li>NEW: donor card + star</li>
                                <li>NEW: ultrite pane + titans pane + upgrades pane (not finalized)</li>
                                <li>NEW: make notifications closeable</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.16.2 - 2021-06-25</div>
                            <ul class="small">
                                <li>FIX: negative resource production</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.16.1 - 2021-06-25</div>
                            <ul class="small">
                                <li>FIX: power and defense star values</li>
                                <li>FIX: +NAN/s value in resource production</li>
                                <li>FIX: EMC negative value</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.16.0 - 2021-06-24</div>
                            <ul class="small">
                                <li>FIX: calculator computed values</li>
                                <li>FIX: computed ship costs after scouting and invasion</li>
                                <li>NEW: nanoswarms DM upgrade will be removed for the moment (those who have it keep it until next rebirth)</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.15.0 - 2021-06-24</div>
                            <ul class="small">
                                <li>FIX: 'Battery Efficiency' still doesn't increase battery storage in v1.14.0</li>
                                <li>FIX: reaching 250 resource machines, or reaching 50T produced resources gives negative XP</li>
                                <li>FIX: nanoswarm resource not showing the resource it is on, after refresh</li>
                                <li>FIX: 'Display autosave notifications' not persisting between refreshes</li>
                                <li>NEW: calculator to compute costs and timers to reach achievements on each machine cards</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.14.0 - 2021-06-24</div>
                            <ul class="small">
                                <li>FIX: 'Battery Efficiency' does not actually increase battery stogage</li>
                                <li>FIX: reset faction relationship to DM upgrade after rebirth</li>
                                <li>NEW: display a warning message when there is not enough consumed resource storage to produce</li>
                                <li>NEW: an option to hide or not locked items</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.13.0 - 2021-06-23</div>
                            <ul class="small">
                                <li>FIX: exit game loop when last update is later than now</li>
                                <li>FIX: reflect boosts in machine cards production/consumptions values</li>
                                <li>FIX: display green mark on 'Batteries' menu item instead of 'Energy' menu item</li>
                                <li>NEW: un-collapse all on 'Rebirth'</li>
                                <li>NEW: display real 'Max' amount of plasma/energy to be converted</li>
                                <li>NEW: when card is minimized, display name + current count</li>
                                <li>NEW: manual save button</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.12.0 - 2021-06-22</div>
                            <ul class="small">
                                <li>FIX: 'Auto-EMC' consumption issue fixed</li>
                                <li>NEW: display total production/consumption and balance on each resource pane</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.11.2 - 2021-06-22</div>
                            <ul class="small">
                                <li>FIX: 'Auto-EMC' frequency issue fixed</li>
                                <li>FIX: 'Multi-Buy' description fixed</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.11.0 - 2021-06-22</div>
                            <ul class="small">
                                <li>NEW: Dyson Segment calculator takes into account current resource count to compute timers</li>
                                <li>NEW: add 'Multi-Buy' as Corporation Kitrinos upgrade</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.10.0 - 2021-06-21</div>
                            <ul class="small">
                                <li>NEW: add Dyson Segment calculator</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.9.2 - 2021-06-21</div>
                            <ul class="small">
                                <li>FIX: fixed 'Starting Storage'</li>
                                <li>FIX: fixed 'Storage Discount'</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.9.1 - 2021-06-21</div>
                            <ul class="small">
                                <li>FIX: make all machine cards collaspable</li>
                                <li>FIX: display 'Auto EMC' as unlocked</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.9.0 - 2021-06-21</div>
                            <ul class="small">
                                <li>NEW: add 'Auto EMC' as Prasnian Empire upgrade</li>
                                <li>NEW: display change log modal when you click on current version number on left side top bar</li>
                                <li>NEW: add 'Hard Reset' functionnality in 'Options' pane</li>
                                <li>NEW: save left side menu group collapse state</li>
                                <li>NEW: make machine card collaspable and save collaspe state</li>
                                <li>NEW: new option to activate/dactivate achievement notification</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.8.0 - 2021-06-20</div>
                            <ul class="small">
                                <li>NEW: better displaying of statictics</li>
                                <li>FIX: display "DONE" on "Floor #2" only when all wonders are activated</li>
                                <li>FIX: "Mystery Wonder Construction" unlocks "Floor #2"</li>
                                <li>FIX: left side resource production displaying is rounding as storage</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.7.0 - 2021-06-19</div>
                            <ul class="small">
                                <li>FIX: Make resource boosts multiplicative, rather than additive</li>
                                <li>FIX : Unlock T5 machines only when Wonder Meteorite is activated</li>
                                <li>NEW: better precision in number displaying (4 digits)</li>
                                <li>NEW: current version number displaying on left side top bar</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.6.0 - 2021-06-18</div>
                            <ul class="small">
                                <li>FIX: fix Energy Efficiency boost (again)</li>
                                <li>NEW : remove dependendy between Wonder Station Floor #2 and Dyson Sphere</li>
                                <li>NEW : add statistics in Achievements pane</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.5.0 - 2021-06-18</div>
                            <ul class="small">
                                <li>NEW : add EMC amount selector</li>
                                <li>NEW : change EMC pane displaying</li>
                                <li>NEW : make Wonder Station Floor #2 available only if you have 1 Dyson Sphere at least (for those who already build wonders on floor #2, you don't loose anything, you will recover your wonders after the first Dyson Sphere)</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.4.0 - 2021-06-18</div>
                            <ul class="small">
                                <li>FIX: fix Energy Efficiency boost</li>
                                <li>FIX: fix Science Efficiency boost</li>
                                <li>NEW: change Ranking pane displaying</li>
                                <li>NEW: change Achievements pane displaying</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.3.0 - 2021-06-17</div>
                            <ul class="small">
                                <li>NEW: add backend to save player current rank data and new pane to display player ranks (leaderboard first tentative)</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.2.0 - 2021-06-16</div>
                            <ul class="small">
                                <li>FIX: to unlock "Floor #1" whatever the wonder you decide to achieve first</li>
                                <li>NEW : make site more compatible with screenreaders</li>
                                <li>NEW : display current version number of the game</li>
                                <li>NEW : every hour check latest version on Github and propose to update the game if current version is not up to date</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.1.0 - 2021-06-16</div>
                            <ul class="small">
                                <li>FIX : do not double the consumption for "Upgrade Resource Technology" & "Upgrade Engine Technology"</li>
                                <li>NEW : display timer to tell when item storage will be empty</li>
                                <li>NEW : display item description even when it is done</li>
                                <li>NEW : display different button style when you hover/click on it</li>
                                <li>NEW : make new achievement toast clickable to achivevement pane</li>
                            </ul>
                        </div>
                        <div class="col-12 border-top">
                            <div class="text-light">v1.0.0 - 2021-06-16</div>
                            <ul class="small">
                                <li>Initial release</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import Header from './components/Header.vue'
import Content from './components/Content.vue'
import SidenavGroup from './components/SidenavGroup.vue'
import SidenavItem from './components/SidenavItem.vue'
import Pane from './components/Pane.vue'
import Card from './components/Card.vue'
import Resource from './components/Resource.vue'
import Buildable from './components/Buildable.vue'
import Emc from './components/Emc.vue'
import Star from './components/Star.vue'
import Fleet from './components/Fleet.vue'
import CalcSegment from './components/CalcSegment.vue'
import CalcBuilding from './components/CalcBuilding.vue'

import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

import { Tooltip, Toast, Modal } from 'bootstrap'

import ghApi from './apis/ghApi.js'

// import axios from 'axios'
import moment from 'moment'

export default {
    components: {

        'top-header': Header,
        'inner-content': Content,
        'sidenav-group': SidenavGroup,
        'sidenav-item': SidenavItem,
        'pane': Pane,
        'card': Card,
        'resource': Resource,
        'buildable': Buildable,
        'emc': Emc,
        'star': Star,
        'fleet': Fleet,
        'calc-segment': CalcSegment,
        'calc-building': CalcBuilding,
    },
    data() {
        return {

            loaded: false,
            sidebarOpen: false,
            defeat: false,
            fastInterval: null,
            slowInterval: null,
            ghInterval: null,

            tooltips: [],

            toastAutoSave: null,
            toastAchievement: null,
            toastSpySuccess: null,
            toastSpyFailed: null,
            toastInvadeSuccess: null,
            toastInvadeFailed: null,
            toastAbsorbSuccess: null,

            showToastAutoSave: true,
            showToastAchievement: true,
            showLockedItems: false,
            showPinnedItems: false,
            showDoneTechs: true,
            showRoadmap: true,

            compressed: null,
            newCompanyName: null,
            autoSavingDuration: null,

            calcId: 'metal',
            activeStar: 'star201',

            spyModal: null,
            invadeModal: null,
            absorbModal: null,
            rebirthModal: null,
            changeLogModal: null,
            hardResetModal: null,
            segmentModal: null,
            calcModal: null,
            enlightenModal: null,
            enlightenSelected: null,
            overlordModal: null,

            currentRelease: '1.29.1',
            ghLatestRelease: null,

            login: null,
            password: null,

            leaderboard_ranks: null,
            leaderboard_stats: null,

            selectedEmcAmount: null,
            selectedAutoEmcInterval: null,
            showEmcShortcut: null,

            titanSource: null,
            titanDestination: null,
        }
    },
    computed: {
        ...mapState([

            'data', 'companyName', 'locale', 'activePane', 'lastUpdateTime', 'autoSaveInterval', 'timeSinceAutoSave', 'rank',
            'resAchievements', 'prodAchievements', 'newAchievement',
            'notifAutoSave', 'notifAchievement', 'displayLockedItems', 'displayPinnedItems', 'displayDoneTechs', 'displayRoadmap',
            'username', 'token',
            'emcAmount', 'autoEmcInterval', 'displayEmcShortcut', 'timeSinceAutoEmc',
            'stats', 'resources', 'pinned', 'titanSwapingCount',
        ]),
        ...mapGetters([

            'isNotif', 'hasNotif',
            'getThreat', 'getSpyChance', 'getInvadeChance', 'getStarPower', 'getStarDefense', 'getStarSpeed',
            'getDMWonders', 'getDMSpheres', 'getDMResearches', 'getDMRank', 'getDMSwarms', 'getPotentialDM',
            'getULStars', 'getULDarkmatter', 'getULStatues', 'getPotentialUL',
            'getStorageCap', 'getStatuesCount', 'getCurrentTitan', 'getNotCurrentTitan', 'getOwnedStarCount',
        ]),
    },
    created() {
        setTimeout(this.start, 1000)
    },
    methods: {
        ...mapMutations([

            'setLocale', 'setActivePane', 'setLastUpdateTime', 'setTimeSinceAutoSave', 'setCompanyName', 'setAutoSaveInterval',
            'setNotifAutoSave', 'setNotifAchievement', 'setDisplayLockedItems', 'setUsername', 'setToken', 'setEmcAmount', 'setTimeSinceAutoEmc', 'setAutoEmcInterval', 'setDisplayEmcShortcut',
            'setDisplayPinnedItems', 'setDisplayDoneTechs', 'setDisplayRoadmap',
        ]),
        ...mapActions([

            'initialize', 'load',
            'computeProdValues', 'produceResources', 'updateTimers', 'checkBoosts', 'updateAchievements', 'save',
            'setActiveShip', 'spy', 'invade', 'absorb',
            'rebirth', 'performAutoEmc', 'enlighten',
            'performAutoStorageUpgrade', 'swapTitan',
        ]),
        momentFormat(date, fmt) {
            return moment(date).format(fmt)
        },
        changeLocale(lang) {

            if (this.$i18n.locale !== lang) {
                this.setLocale(lang)
                this.$i18n.locale = lang
            }
        },
        start() {

            this.initialize()
            this.load()

            this.changeLocale(this.locale)
            this.newCompanyName = this.companyName
            this.autoSavingDuration = this.autoSaveInterval / 1000
            this.login = this.username
            this.selectedEmcAmount = this.emcAmount
            this.selectedAutoEmcInterval = this.autoEmcInterval / 1000

            // this.ghUpdate()

            this.fastInterval = setInterval(() => { this.fastUpdate() }, 100)
            this.slowInterval = setInterval(() => { this.slowUpdate() }, 1000)
            // this.ghInterval = setInterval(() => { this.ghUpdate() }, 3600000)

            this.loaded = true

            this.$nextTick(() => {

                let element = null

                element = document.getElementById('toastAutoSave')
                this.toastAutoSave = new Toast(element)
                this.showToastAutoSave = this.notifAutoSave
                this.showToastAchievement = this.notifAchievement
                this.showLockedItems = this.displayLockedItems
                this.showPinnedItems = this.displayPinnedItems
                this.showDoneTechs = this.displayDoneTechs
                this.showRoadmap = this.displayRoadmap
                this.showEmcShortcut = this.displayEmcShortcut
                element = document.getElementById('toastAchievement')
                this.toastAchievement = new Toast(element)

                element = document.getElementById('toastSpySuccess')
                this.toastSpySuccess = new Toast(element)

                element = document.getElementById('toastSpyFailed')
                this.toastSpyFailed = new Toast(element)

                element = document.getElementById('toastInvadeSuccess')
                this.toastInvadeSuccess = new Toast(element)

                element = document.getElementById('toastInvadeFailed')
                this.toastInvadeFailed = new Toast(element)

                element = document.getElementById('toastAbsorbSuccess')
                this.toastAbsorbSuccess = new Toast(element)

                Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]')).forEach(node => this.tooltips.push(new Tooltip(node)))

                element = document.getElementById('spyModal')
                this.spyModal = new Modal(element)

                element = document.getElementById('invadeModal')
                this.invadeModal = new Modal(element)

                element = document.getElementById('absorbModal')
                this.absorbModal = new Modal(element)

                element = document.getElementById('rebirthModal')
                this.rebirthModal = new Modal(element)

                element = document.getElementById('changeLogModal')
                this.changeLogModal = new Modal(element)

                element = document.getElementById('hardResetModal')
                this.hardResetModal = new Modal(element)

                element = document.getElementById('segmentModal')
                this.segmentModal = new Modal(element)

                element = document.getElementById('calcModal')
                this.calcModal = new Modal(element)

                element = document.getElementById('enlightenModal')
                this.enlightenModal = new Modal(element)

                element = document.getElementById('overlordModal')
                this.overlordModal = new Modal(element)
            })
        },
        fastUpdate() {

            let currentTime = new Date().getTime()
            let delta = (currentTime - this.lastUpdateTime) / 1000
            if (delta <= 0) {
                this.setLastUpdateTime(currentTime)
                return
            }

            if (delta < (1 / 60)) return

            this.setLastUpdateTime(currentTime)
            this.setTimeSinceAutoSave(this.timeSinceAutoSave + delta)
            this.setTimeSinceAutoEmc(this.timeSinceAutoEmc + delta)

            this.computeProdValues()
            this.performAutoStorageUpgrade()
            this.produceResources(delta)
            this.updateTimers()
            this.checkBoosts()

            let autoEmcCount = Math.floor((this.timeSinceAutoEmc * 1000) / this.autoEmcInterval)
            for (let i = 0; i < autoEmcCount; i++) this.performAutoEmc()
            if (autoEmcCount > 0) this.setTimeSinceAutoEmc(0)
        },
        slowUpdate() {

            this.updateAchievements()
            if (this.newAchievement == true && this.showToastAchievement == true) this.toastAchievement.show()

            let timeLeft = this.autoSaveInterval - (this.timeSinceAutoSave * 1000)
            if (this.autoSaveInterval < 0) timeLeft = 1000
            if (timeLeft < 100) {

                this.save()
                this.setTimeSinceAutoSave(1)
                if (this.showToastAutoSave) this.toastAutoSave.show()

                if (this.token) {

                    // let data = {
                    //     rank: this.rank,
                    //     stats: this.stats,
                    // }
                    // axios.post('https://ngspacecompany.exileng.com/api/post/', data, { headers: { 'Authorization': 'Token ' +  this.token }})
                }

                // axios.get('https://ngspacecompany.exileng.com/api/ranks/').then((response) => { this.leaderboard_ranks = response.data })
                // axios.get('https://ngspacecompany.exileng.com/api/stats/').then((response) => { this.leaderboard_stats = response.data })
            }
        },
        ghUpdate() {

            ghApi
                .get('/repos/ExileNG/NGSpaceCompany/releases/latest')
                .then((response) => { this.ghLatestRelease = response.data.tag_name })
        },
        exportData() {

            let text = localStorage.getItem('ngsavecrypted')
            this.compressed = text
        },
        importData() {

            if (!this.compressed || !this.compressed.trim()) return console.warn('No data to import')
            if (this.compressed.length % 4 !== 0) return console.warn('Data corrupted')

            localStorage.setItem('ngsavecrypted', this.compressed)

            window.location.reload()
        },
        onSpy() {

            this.spy(this.activeStar).then(result => {
                if (result == true) this.toastSpySuccess.show()
                else this.toastSpyFailed.show()
            })
        },
        onInvade() {

            this.invade(this.activeStar).then(result => {
                if (result == true) this.toastInvadeSuccess.show()
                else this.toastInvadeFailed.show()
            })
        },
        onAbsorb() {

            this.absorb(this.activeStar).then(result => {
                if (result == true) this.toastAbsorbSuccess.show()
            })
        },
        onRebirth() {

            this.loaded = true

            this.rebirth().then(result => {
                if (result == true) window.location.reload()
            })
        },
        onRefresh() {

            this.save()
            this.setTimeSinceAutoSave(1)

            window.location.reload()
        },
        onConnect(login, pwd) {
          console.log(login, pwd)
            // if (login && login.trim().length > 4 && pwd && pwd.trim().length > 4)
                // axios.post('https://ngspacecompany.exileng.com/api/register/', { username:login.trim(), password:pwd.trim() })
                //     .then((response) => {
                //
                //         this.setUsername(login.trim())
                //         this.setToken(response.data.token)
                //     })
                //     .catch(() => {
                //
                //         axios.post('https://ngspacecompany.exileng.com/api/login/', { username:login.trim(), password:pwd.trim() })
                //             .then((response) => {
                //
                //                 this.setUsername(login.trim())
                //                 this.setToken(response.data.token)
                //             })
                //             .catch((error) => {
                //
                //                 console.log(error.response.data)
                //             })
                //     })
        },
        onDisconnect() {

            this.setUsername(null)
            this.setToken(null)
        },
        onHardReset() {

            this.loaded = true

            localStorage.removeItem('ngsave')
            localStorage.removeItem('ngsavecrypted')

            window.location.reload()
        },
        onSave() {

            this.save()
            this.setTimeSinceAutoSave(1)
            if (this.showToastAutoSave) this.toastAutoSave.show()
        },
        onEnlighten() {

            this.enlighten(this.enlightenSelected).then(result => {
                if (result == true) {
                    this.loaded = true
                    this.enlightenSelected = null
                    window.location.reload()
                }
            })
        },
    },
    beforeUnmount() {

        delete this.toastAutoSave
        delete this.toastAchievement
        delete this.toastSpySuccess
        delete this.toastSpyFailed
        delete this.toastInvadeSuccess
        delete this.toastInvadeFailed
        delete this.toastAbsorbSuccess

        delete this.tooltips

        delete this.spyModal
        delete this.invadeModal
        delete this.absorbModal
        delete this.rebirthModal
        delete this.changeLogModal
        delete this.hardResetModal
        delete this.segmentModal
        delete this.calcModal
        delete this.enlightenModal
        delete this.overlordModal
        clearInterval(this.fastInterval)
        clearInterval(this.slowInterval)
        clearInterval(this.ghInterval)
    },
}
</script>
